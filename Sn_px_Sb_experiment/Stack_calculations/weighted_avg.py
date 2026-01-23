import numpy as np
import pandas as pd
from pathlib import Path
from scipy.interpolate import PchipInterpolator

# ============================================================
# SETTINGS (EDIT THESE)
# ============================================================

FLUX_DIR = Path("/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/Flux_55MeV")
FLUX_PATTERN = "*_fluxes.csv"

# Try "," first; if your files are whitespace-separated, change to: SEP = r"\s+"
SEP = ","

# Expected columns in the flux files
COL_NAME = "name"
COL_E = "energy"
COL_PHI = "flux"

# Cross section monitor files
XS_FILES = {
    "Co56": Path("/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/cup56cot.txt"),
    "Co58": Path("/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/cup58cot.txt"),
    "Zn62": Path("/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/cup62znt.txt"),
    "Zn63": Path("/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/cup63znt.txt"),
    "Zn65": Path("/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/cup65znt.txt"),
}
XS_SKIPROWS = 6

OUT_CSV = FLUX_DIR / "weighted_avg_cross_sections_all_flux_files.csv"


# ============================================================
# FUNCTIONS
# ============================================================

def load_xs_interpolator(xs_path: Path, skiprows: int = 0):
    data = np.loadtxt(xs_path, skiprows=skiprows)
    E = data[:, 0].astype(float)
    sigma = data[:, 1].astype(float)

    order = np.argsort(E)
    E = E[order]
    sigma = sigma[order]

    E_unique, idx = np.unique(E, return_index=True)
    sigma_unique = sigma[idx]

    return PchipInterpolator(E_unique, sigma_unique, extrapolate=False)

def weighted_avg_sigma(interp_sigma, E, phi):
    sig = interp_sigma(E)
    sig = np.where(np.isfinite(sig), sig, 0.0)
    num = np.trapz(sig * phi, E)
    den = np.trapz(phi, E)
    return num / den if den != 0 else np.nan

def read_flux_file_strict(path: Path) -> pd.DataFrame:
    """
    Strict reader:
    - forces columns: name, energy, flux
    - fails loudly if energy/flux can't be converted to float
    - prints helpful debug info before raising
    """
    df = pd.read_csv(path, sep=SEP, engine="python")

    # Fail early if columns aren't what we expect
    missing = {COL_NAME, COL_E, COL_PHI} - set(df.columns)
    if missing:
        print("\n--- COLUMN MISMATCH ---")
        print("File:", path.name)
        print("Columns found:", df.columns.tolist())
        raise ValueError(f"{path.name}: missing expected columns {missing}")

    # Convert to numeric, but FAIL if any non-numeric exists
    try:
        df[COL_E] = pd.to_numeric(df[COL_E], errors="raise")
        df[COL_PHI] = pd.to_numeric(df[COL_PHI], errors="raise")
    except Exception as e:
        print("\n--- NON-NUMERIC FOUND DURING CONVERSION ---")
        print("File:", path.name)
        print("Columns:", df.columns.tolist())

        # show a few suspicious entries (where coercion would fail)
        e_bad = pd.to_numeric(df[COL_E], errors="coerce").isna()
        p_bad = pd.to_numeric(df[COL_PHI], errors="coerce").isna()

        if e_bad.any():
            print("\nBad energy values (unique, first 20):",
                  df.loc[e_bad, COL_E].astype(str).unique()[:20])
            print(df.loc[e_bad, [COL_NAME, COL_E, COL_PHI]].head(10))

        if p_bad.any():
            print("\nBad flux values (unique, first 20):",
                  df.loc[p_bad, COL_PHI].astype(str).unique()[:20])
            print(df.loc[p_bad, [COL_NAME, COL_E, COL_PHI]].head(10))

        raise

    return df[[COL_NAME, COL_E, COL_PHI]].copy()


# ============================================================
# MAIN
# ============================================================

# Build interpolators
xs_interp = {rxn: load_xs_interpolator(p, skiprows=XS_SKIPROWS) for rxn, p in XS_FILES.items()}

# Find flux files
flux_files = sorted(FLUX_DIR.glob(FLUX_PATTERN))
print(f"Found {len(flux_files)} flux files in {FLUX_DIR} matching '{FLUX_PATTERN}'")
if not flux_files:
    raise FileNotFoundError(f"No files matched '{FLUX_PATTERN}' in {FLUX_DIR}")

rows = []
for f in flux_files:
    flux_df = read_flux_file_strict(f)

    for name, g in flux_df.groupby(COL_NAME, sort=True):
        g = g.sort_values(COL_E)

        # these will be guaranteed numeric now
        E = g[COL_E].to_numpy(dtype=float)
        phi = g[COL_PHI].to_numpy(dtype=float)

        row = {
            "file": f.name,
            "name": str(name),
            "E_min": float(E.min()),
            "E_max": float(E.max()),
            "phi_int": float(np.trapz(phi, E)),
        }

        for rxn, interp in xs_interp.items():
            row[f"<sigma>_{rxn}"] = float(weighted_avg_sigma(interp, E, phi))

        rows.append(row)

out = pd.DataFrame(rows).sort_values(["file", "name"]).reset_index(drop=True)
out.to_csv(OUT_CSV, index=False)
print(f"Saved: {OUT_CSV}")
print(out.head())
