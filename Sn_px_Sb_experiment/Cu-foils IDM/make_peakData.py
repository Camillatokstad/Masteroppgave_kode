import curie as ci
import numpy as np
from pathlib import Path
import pandas as pd


ISOTOPES = [
    "62CU", "60CU", "63ZN", "61CO", "61CU", "58COm",
    "62ZN", "64CU", "58CO", "65ZN", "56CO", "57CO", "64ZN",
    "62NI", "60NI", "61NI", "59NI", "57NI", "56NI", "54MN", "60CO", "69ZNm",
]

# mønster på filnavn til gjennkjenning, HUSK Å ENNDRE HVIS DU ENDRER FILNAVN
SPE_PATTERN = "*_Cu*_IDM.Spe"

# få det inn i riktig mappe, HUSK Å ENDRE HVIS DU ENDRER MAPPE
this_dir = Path(__file__).resolve().parent
dest_dir = this_dir.parent / "Decay_EoB" / "test"
dest_dir.mkdir(parents=True, exist_ok=True)

# cache calibrations
_calibration_cache = {}

# ønsket kolonnerekkefølge
DESIRED_COLUMNS = [
    "filename",
    "isotope",
    "energy",
    "counts",
    "unc_counts",
    "intensity",
    "unc_intensity",
    "efficiency",
    "unc_efficiency",
    "decays",
    "unc_decays",
    "decay_rate",
    "unc_decay_rate",
    "chi2",
    "start_time",
    "live_time",
    "real_time",
]


# finne avstanden i navnet på spekterne, og returne som en string
def get_distance_cm_from_name(path: Path) -> str:
    stem = path.stem  # eksempel på filnavn 'AB09232025_Cu09_52cm_IDM'
    parts = stem.split("_")  # splitter filnavnet
    # finner delen som slutter med cm
    dist_part = None
    for p in parts:
        if p.endswith("cm"):
            dist_part = p
            break
    if dist_part is None:
        raise ValueError(f"Could not find '*cm' in filename: {path.name}")
    # '52cm' -> '52'
    return dist_part.replace("cm", "")


# load calibration i gitte avstander i cm, bruker cache for å kun hente filene én gang
def get_calibration_for_distance(distance_cm: str) -> ci.Calibration:
    if distance_cm in _calibration_cache:
        return _calibration_cache[distance_cm]

    calib_name = f"calibration_IDM_{distance_cm}cm.json"
    calib_path = this_dir / calib_name

    if not calib_path.exists():
        raise FileNotFoundError(
            f"Calibration file not found: {calib_path}\n"
            f"Expected format: calibration_IDM_{distance_cm}cm.json"
        )

    cb = ci.Calibration(str(calib_path))
    _calibration_cache[distance_cm] = cb
    return cb


def clean_paths_in_csv(csv_path: Path):
    """
    Etter at peakData-CSV er laget:
    - fjern fulle paths i filnavn-kolonner (.Spe),
    - la start_time / dato-kolonner være i fred.
    """
    df = pd.read_csv(csv_path)

    for col in df.select_dtypes(include=["object"]).columns:
        if col == "start_time":
            # VIKTIG: ikke rør start_time – Curie har allerede riktig format
            continue

        series = df[col].dropna().astype(str)
        if series.empty:
            continue

        # ser dette ut som en filnavn-kolonne? (slutter på .Spe / .spe)
        mask = series.str.contains(r"\.Spe$", case=False)
        if mask.mean() > 0.8:
            df[col] = df[col].astype(str).apply(lambda s: Path(s).name)

    df.to_csv(csv_path, index=False)



# Leser spekterne, kalibrerer med riktig kalibreringsfiler og fitter peaker med ISOTOPES
def process_spectrum(spe_path: Path):
    """
    Read a .Spe file, apply calibration + isotopes, and save peakData CSV to dest_dir.
    """
    print(f"\n=== Processing {spe_path.name} ===")

    # kalibrering utifra distanse
    distance = get_distance_cm_from_name(spe_path)  # f.eks. '52'
    cb = get_calibration_for_distance(distance)

    # fitter peaks
    print(f"  Using calibration: calibration_IDM_{distance}cm.json")
    spe = ci.Spectrum(str(spe_path))
    spe.cb = cb
    spe.isotopes = ISOTOPES

    # spe.plot()

    # gir et output navn til peakData fila
    out_name = dest_dir / f"{spe_path.stem}_IDM_peakData.csv"

    spe.saveas(str(out_name))
    print(f"  Saved peakData -> {out_name}")

    # rens opp filename-kolonnen og kolonnerekkefølgen
    clean_paths_in_csv(out_name)
    print(f"  Cleaned & ordered columns -> {out_name.name}")


def main():
    spe_files = sorted(this_dir.glob(SPE_PATTERN))
    if not spe_files:
        print(f"No spectra found matching pattern: {SPE_PATTERN}")
        return

    print(f"Found {len(spe_files)} spectra:")
    for f in spe_files:
        print(" ", f.name)

    for spe_path in spe_files:
        process_spectrum(spe_path)

    print("\nAll spectra processed.")


if __name__ == "__main__":
    main()
