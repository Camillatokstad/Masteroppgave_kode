import curie as ci
import numpy as np
from pathlib import Path
import pandas as pd   # for editing the CSV


# --- felles oppsett ---

cb = ci.Calibration("calibration_Det2_50cm.json")


ISOTOPES = [
    "62CU", "60CU", "63ZN", "61CO", "61CU", "58COm",
    "62ZN", "64CU", "58CO", "65ZN", "56CO", "57CO", "64ZN",
    "62NI", "60NI", "61NI", "59NI", "57NI", "56NI", "54MN",
    "60CO", "69ZNm", "66GA",
]


# 50 cm
SPE_FILES = [
    "AN09232025_Cu08_50cm_DET2.Spe",
    "BD09242025_Cu10_50cm_DET2.Spe",
]


this_dir = Path(__file__).resolve().parent
dest_dir = this_dir.parent / "Decay_EoB" / "Cu"
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

    spe = ci.Spectrum(str(spe_path))
    spe.cb = cb
    spe.isotopes = ISOTOPES

    spe.plot()  # hvis du vil se plott

    spe.summarize()  # kjører peakfitting og lager data

    out_name = dest_dir / f"{spe_path.stem}_peakData.csv"
    spe.saveas(str(out_name))
    print(f"  Saved peakData -> {out_name}")

    # Rydd opp i 'filename' inne i CSV
    clean_filename_column(out_name)
    print(f"  Cleaned filename column -> {out_name.name}")


def main():
    for spe_filename in SPE_FILES:
        process_one_spectrum(spe_filename)

    print("\nAll spectra processed.")


if __name__ == "__main__":
    main()
