import curie as ci
import numpy as np
from pathlib import Path
import pandas as pd   # for editing the CSV


# --- felles oppsett ---

cb = ci.Calibration("calibration_Det2_10cm.json")


ISOTOPES = [
    "57NI","60CU","56CO","56NI",'58CO', '57CO', '55CO' 
]


# 10 cm
SPE_FILES = [
    "FS09302025_Ni01_10cm_Det2.Spe",
    "GN10142025_Ni07_10cm_Det2.Spe",
]

this_dir = Path(__file__).resolve().parent
dest_dir = this_dir.parent / "Decay_EoB" / "Ni"
dest_dir.mkdir(parents=True, exist_ok=True)

# funksjon sånn at jeg kun får filnavn i csv-filen, og ikke hele pathen 
def clean_filename_column(csv_path: Path):
    df = pd.read_csv(csv_path)
    if "filename" in df.columns:
        df["filename"] = df["filename"].astype(str).apply(lambda s: Path(s).name)
    df.to_csv(csv_path, index=False)


def process_one_spectrum(spe_filename: str):
    print(f"\n=== Processing {spe_filename} ===")

    spe_path = this_dir / spe_filename
    if not spe_path.exists():
        raise FileNotFoundError(f"Could not find spectrum file: {spe_path}")

    print(f"Reading Spectrum {spe_path}")
    spe = ci.Spectrum(str(spe_path))
    spe.cb = cb
    spe.isotopes = ISOTOPES

    # At this point Curie has either found peaks or left spe.peaks as None

    peaks = getattr(spe, "peaks", None)
    if peaks is None or getattr(peaks, "empty", False):
        # spe_filename is a string, so use spe_path.name here
        print(f"  No peaks found for {spe_path.name} – skipping CSV.")
        return

    out_name = dest_dir / f"{spe_path.stem}_peakData.csv"
    spe.saveas(str(out_name))
    print(f"  Saved peakData -> {out_name}")

    # Rydd opp i 'filename' inne i CSV
    clean_filename_column(out_name)
    print(f"  Cleaned filename column -> {out_name.name}")

    # Optional:
    spe.plot()  # hvis du vil se plott



def main():
    for spe_filename in SPE_FILES:
        process_one_spectrum(spe_filename)

    print("\nAll spectra processed.")


if __name__ == "__main__":
    main()
