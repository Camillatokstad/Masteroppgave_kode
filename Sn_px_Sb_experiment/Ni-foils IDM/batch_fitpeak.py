import curie as ci
import numpy as np
from pathlib import Path
import pandas as pd   # for editing the CSV


# --- felles oppsett ---

cb = ci.Calibration("calibration_IDM_45cm.json")
#cb = ci.Calibration("calibration_IDM_10cm.json")
#cb = ci.Calibration("calibration_IDM_30cm.json")
#cb = ci.Calibration("calibration_IDM_25cm.json")
#cb = ci.Calibration("calibration_IDM_15cm.json")
#cb = ci.Calibration("calibration_IDM_20cm.json")





ISOTOPES = [
    "57NI","60CU","56CO","56NI",'58CO', '57CO', '55CO' 
]



# 45 cm 
SPE_FILES = [
    "AO09232025_Ni08_45cm_IDM.Spe",
    "AP09242025_Ni09_45cm_IDM.Spe",
    "AQ09242025_Ni10_45cm_IDM.Spe",
   
]

"""
# 30 cm 
SPE_FILES = [
    "AR09242025_Ni11_30cm_IDM.Spe",
    "AS09242025_Ni12_30cm_IDM.Spe",
    "BQ09242025_Ni08_30cm_IDM.Spe",
    "CF09242025_Ni01_30cm_IDM.Spe",
    "CG09242025_Ni02_30cm_IDM.Spe",
    "CH09242025_Ni03_30cm_IDM.Spe",
    "CI09242025_Ni04_30cm_IDM.Spe",
    "DH09252025_Ni01_30cm_IDM.Spe",
    "DI09252025_Ni02_30cm_IDM.Spe",
    "DJ09252025_Ni03_30cm_IDM.Spe",
    "DK09252025_Ni04_30cm_IDM.Spe",
    "DL09252025_Ni05_30cm_IDM.Spe",
    "DM09252025_Ni06_30cm_IDM.Spe",
    "DN09252025_Ni07_30cm_IDM.Spe",
    "DO09252025_Ni08_30cm_IDM.Spe",
    "DP09252025_Ni09_30cm_IDM.Spe", 
]


# 25 cm
SPE_FILES = [
    "AT09242025_Ni13_25cm_IDM.Spe",
    "CJ09242025_Ni05_25cm_IDM.Spe",
    "CK09242025_Ni06_25cm_IDM.Spe",
    "CL09242025_Ni07_25cm_IDM.Spe",
    "CT09252025_Ni08_25cm_IDM.Spe",
    "CU09252025_Ni09_25cm_IDM.Spe",
    "CV09252025_Ni10_25cm_IDM.Spe",
    "CW09252025_Ni11_25cm_IDM.Spe",
    "CX09252025_Ni12_25cm_IDM.Spe",
]

# 20 cm
SPE_FILES = [
    "EB09262025_Ni11_20cm_IDM.Spe",
    "EC09262025_Ni10_20cm_IDM.Spe",
    "ED09262025_Ni09_20cm_IDM.Spe",
    "EE09262025_Ni08_20cm_IDM.Spe",
]


# 15 cm
SPE_FILES = [
    "AU09242025_Ni14_15cm_IDM.Spe",
    "E09262025_Ni03_15cm_IDM.Spe",
    "EM09262025_Ni07_15cm_IDM.Spe",
    "EN09262025_Ni06_15cm_IDM.Spe",
    "EO09262025_Ni05_15cm_IDM.Spe",
    "EP09262025_Ni04_15cm_IDM.Spe",
    "EQ09262025_Ni03_15cm_IDM.Spe",
    "ER09262025_Ni02_15cm_IDM.Spe",
    "ES09262025_Ni01_15cm_IDM.Spe",
    "CY09252025_Ni13_15cm_IDM.Spe"
]


# 10 cm
SPE_FILES = [
    "CZ09252025_Ni14_10cm_IDM.Spe",
    "DX09252025_Ni14_10cm_IDM.Spe",
    "DY09262025_Ni13_10cm_IDM.Spe",
    "DZ09262025_Ni12_10cm_IDM.Spe",
    "EA09262025_Ni14_10cm_IDM.Spe",
    "FI09282025_Ni14_10cm_IDM.Spe",
    "FJ09282025_Ni13_10cm_IDM.Spe",
    "FK09282025_Ni12_10cm_IDM.Spe",
    "FL09282025_Ni11_10cm_IDM.Spe",
    "FN09292025_Ni10_10cm_IDM.Spe",
    "FO09292025_Ni09_10cm_IDM.Spe",
    "FP09292025_Ni08_10cm_IDM.Spe",
    "FQ09292025_Ni07_10cm_IDM.Spe",
    "FR09292025_Ni06_10cm_IDM.Spe",
    "FT09302025_Ni05_10cm_IDM.Spe",
    "FU09302025_Ni04_10cm_IDM.Spe",
    "FV09302025_Ni03_10cm_IDM.Spe",
    "FW09302025_Ni02_10cm_IDM.Spe",
]
"""

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
