import numpy as np
import pandas as pd
from pathlib import Path
from scipy.interpolate import PchipInterpolator

flux_dir = Path("/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/Flux_55MeV")
flux_pattern = "*_fluxes.csv"
sep = ","

xs_mon = {
    "Co56": "/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/cup56cot.txt",
    "Co58": "/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/cup58cot.txt",
    "Zn62": "/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/cup62znt.txt",
    "Zn63": "/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/cup63znt.txt",
    "Zn65": "/Users/camillatokstad/Documents/FA/Masteroppgave/Sn_px_Sb_experiment/Stack_calculations/cup65znt.txt",
}


def xs_interp(path):
    data = np.loadtxt(path, skiprows=6, usecols=(0, 1))
    E = data[:, 0]
    xs = data[:, 1]

    order = np.argsort(E)
    E, xs = E[order], xs[order] #sort by energy

    E, idx = np.unique(E, return_index=True) #remove duplicate energies
    return PchipInterpolator(E, xs[idx], extrapolate=False) 

def weighted_avg_xs(f, E, phi):
    sig = f(E)
    sig = np.where(np.isfinite(sig), sig, 0.0) #every point outside interpolation range gets xs=0
    den = np.trapz(phi, E)
    num = np.trapz(sig * phi, E)
    return num / den if den != 0 else np.nan

interps = {k: xs_interp(v) for k, v in xs_mon.items()} #create interpolators for each reaction

rows = []
for file in sorted(flux_dir.glob(flux_pattern)):

    df = pd.read_csv(file, sep=sep, engine="python", usecols=["name", "energy", "flux"])
    df["energy"] = pd.to_numeric(df["energy"], errors="raise")
    df["flux"]   = pd.to_numeric(df["flux"], errors="raise")

    df = df[df["name"].astype(str).str.match(r"Cu")]

    for name, g in df.groupby("name", sort=True):
        g = g.sort_values("energy")
        E = g["energy"].to_numpy()
        phi = g["flux"].to_numpy()

        row = {
            "file": file.name,
            "name": name,
            "E_min": float(E.min()),
            "E_max": float(E.max()),
            "phi_int": float(np.trapz(phi, E)),
        }
        row.update({f"<xs> for {rxn}": float(weighted_avg_xs(interps[rxn], E, phi)) for rxn in interps})
        rows.append(row)

out = pd.DataFrame(rows).sort_values(["file", "name"])
out.to_csv(flux_dir / "weighted_avg_cross_sections_55MeV_flux_files.csv", index=False)
print(out.head())
