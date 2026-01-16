import curie as ci
import numpy as np
from pathlib import Path
import pandas as pd   # for editing the CSV


# --- felles oppsett ---

#cb = ci.Calibration("calibration_IDM_45cm.json")
#cb = ci.Calibration("calibration_IDM_52cm.json")
cb = ci.Calibration("calibration_IDM_10cm.json")
#cb = ci.Calibration("calibration_IDM_30cm.json")
#cb = ci.Calibration("calibration_IDM_40cm.json")



ISOTOPES = [
    "62CU", "60CU", "63ZN", "61CO", "61CU", "58COm",
    "62ZN", "64CU", "58CO", "65ZN", "56CO", "57CO", "64ZN",
    "62NI", "60NI", "61NI", "59NI", "57NI", "56NI", "54MN",
    "60CO", "69ZNm", "66GA",
]


"""
# 52 cm 
SPE_FILES = [
    "BR09242025_Cu01_52cm_IDM.Spe",
    "BY09242025_Cu01_52cm_IDM.Spe",
    "BS09242025_Cu02_52cm_IDM.Spe",
    "BT09242025_Cu03_52cm_IDM.Spe",
    "BU09242025_Cu04_52cm_IDM.Spe",
    "BV09242025_Cu05_52cm_IDM.Spe",
    "BX09242025_Cu07_52cm_IDM.Spe",
    "AB09232025_Cu09_52cm_IDM.Spe",
    "AC09232025_Cu10_52cm_IDM.Spe",
    "AE09232025_Cu12_52cm_IDM.Spe",
    "AF09232025_Cu13_52cm_IDM.Spe",
    "AG09232025_Cu14_52cm_IDM.Spe",
    "BW09242025_Cu06_52cm_IDM.Spe",
]

# 45 cm 
SPE_FILES = [
    "CD09242025_Cu06_45cm_IDM.Spe",
    "CE09242025_Cu07_45cm_IDM.Spe",
    "BZ09242025_Cu02_45cm_IDM.Spe",
    "CA09242025_Cu03_45cm_IDM.Spe",
    "CB09242025_Cu04_45cm_IDM.Spe",
    "CC09242025_Cu05_45cm_IDM.Spe",
    "AH09232025_Cu08_45cm_IDM.Spe",
    "AI09232025_Cu09_45cm_IDM.Spe",
    "AJ09232025_Cu10_45cm_IDM.Spe",
    "AD09232025_Cu11_45cm_IDM.Spe",
]

# 40 cm 
SPE_FILES = [
    "CM09242025_Cu01_40cm_IDM.Spe",
    "CN09242025_Cu02_40cm_IDM.Spe",
    'CO09242025_Cu03_40cm_IDM.Spe',
    'CP09242025_Cu04_40cm_IDM.Spe',
    'CQ09252025_Cu05_40cm_IDM.Spe',
    'CR09252025_Cu06_40cm_IDM.Spe',
    'CS09252025_Cu07_40cm_IDM.Spe',
    'AK09232025_Cu11_40cm_IDM.Spe',
    'AL09232025_Cu12_40cm_IDM.Spe',
    'AM09232025_Cu13_40cm_IDM.Spe',

]

# 30 cm
SPE_FILES = [
    "DA09252025_Cu01_30cm_IDM.Spe",
    "DB09252025_Cu02_30cm_IDM.Spe",
    "DC09252025_Cu03_30cm_IDM.Spe",
    "DD09252025_Cu04_30cm_IDM.Spe",
    "DE09252025_Cu05_30cm_IDM.Spe",
    "DF09252025_Cu06_30cm_IDM.Spe",
    "DG09252025_Cu07_30cm_IDM.Spe",
    "BJ09242025_Cu08_30cm_IDM.Spe",
    "BK09242025_Cu09_30cm_IDM.Spe",
    "BL09242025_Cu10_30cm_IDM.Spe",
    "BM09242025_Cu11_30cm_IDM.Spe",
    "AN09232025_Cu14_30cm_IDM.Spe",
]

"""
# 10 cm
SPE_FILES = [
    "EL09262025_Cu01_10cm_IDM.Spe",
    "FH09282025_Cu01_10cm_IDM.Spe",
    "EK09262025_Cu02_10cm_IDM.Spe",
    "FG09282025_Cu02_10cm_IDM.Spe",
    "EJ09262025_Cu03_10cm_IDM.Spe",
    "FF09282025_Cu03_10cm_IDM.Spe",
    "EI09262025_Cu04_10cm_IDM.Spe",
    "FD09272025_Cu04_10cm_IDM.Spe",
    "EH09262025_Cu05_10cm_IDM.Spe",
    "FC09272025_Cu05_10cm_IDM.Spe",
    "EG09262025_Cu06_10cm_IDM.Spe",
    "FB09272025_Cu06_10cm_IDM.Spe",
    "EF09262025_Cu07_10cm_IDM.Spe",
    "FA09272025_Cu07_10cm_IDM.Spe",
    "DW09252025_Cu08_10cm_IDM.Spe",
    "EZ09272025_Cu08_10cm_IDM.Spe",
    "DV09252025_Cu09_10cm_IDM.Spe",
    "EY09272025_Cu09_10cm_IDM.Spe",
    "DU09252025_Cu10_10cm_IDM.Spe",
    "EX09272025_Cu10_10cm_IDM.Spe",
    "DT09252025_Cu11_10cm_IDM.Spe",
    "EW09272025_Cu11_10cm_IDM.Spe",
    "DS09252025_Cu12_10cm_IDM.Spe",
    "EV09272025_Cu12_10cm_IDM.Spe",
    "DR09252025_Cu13_10cm_IDM.Spe",
    "EU09272025_Cu13_10cm_IDM.Spe",
    "DQ09252025_Cu14_10cm_IDM.Spe",
    "ET09262025_Cu14_10cm_IDM.Spe",
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

    #spe.plot()  # hvis du vil se plott

    #spe.summarize()  # kjører peakfitting og lager data

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
