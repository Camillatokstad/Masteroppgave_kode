import matplotlib.pyplot as plt
import pandas as pd
import curie as ci
import json
from pathlib import Path


# Importer JSON-filer

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


# Slå sammen peakData csv-filer til én csv-fil per folie 

def combine_peak_files_for_sample(sample_conf):
    name = sample_conf["name"]
    pattern = sample_conf["peak_file_pattern"]

    files = sorted(Path(".").glob(pattern))
    if not files:
        raise FileNotFoundError(f"No peakData files matched pattern {pattern} for sample {name}")

    dfs = [pd.read_csv(f) for f in files]
    df_concat = pd.concat(dfs, ignore_index=True)

    combined_name = f"{name}_IDM_peakData_combined.csv"
    df_concat.to_csv(combined_name, index=False)
    return combined_name


# Decay analyse for ett isotop i én folie

def analyze_one_isotope_one_sample(sample_conf, isotope_conf, combined_csv):
    """
    Run DecayChain for a single (sample, isotope) pair.
    Returns dict with results.
    If there are no peaks / no counts for that isotope, returns NaNs.
    """
    sample_name = sample_conf["name"]
    EoB = sample_conf["EoB"]              # already in '%m/%d/%Y %H:%M:%S'
    units = sample_conf.get("units", "h")

    isotope_name = isotope_conf["name"]
    A0_guess = isotope_conf.get("A0_guess", sample_conf["A0_guess"])

    # --- 1) load peakData once ---
    df_peaks = pd.read_csv(combined_csv)

    # a) check if this isotope exists at all
    if "isotope" in df_peaks.columns:
        isotopes_present = set(df_peaks["isotope"].unique())
        if isotope_name not in isotopes_present:
            print(f"{sample_name} – {isotope_name}: no peaks in {combined_csv}, skipping fit.")
            return {
                "sample": sample_name,
                "isotope": isotope_name,
                "EoB": EoB,
                "units": units,
                "A0_parent": float("nan"),
                "A0_err_parent": float("nan"),
                "A0_vector": [],
                "cov_A0": [],
                "plot_file": None,
                "peak_data_file": combined_csv,
            }
    else:
        print(f"Warning: 'isotope' column not found in {combined_csv}; trying fit anyway.")

    # b) build explicit list of spectra filenames from the CSV
    if "filename" not in df_peaks.columns:
        raise KeyError(f"'filename' column not found in {combined_csv}")

    spectra_list = sorted(df_peaks["filename"].astype(str).unique())
    if not spectra_list:
        print(f"{sample_name}: no filenames found in {combined_csv}, skipping all isotopes.")
        return {
            "sample": sample_name,
            "isotope": isotope_name,
            "EoB": EoB,
            "units": units,
            "A0_parent": float("nan"),
            "A0_err_parent": float("nan"),
            "A0_vector": [],
            "cov_A0": [],
            "plot_file": None,
            "peak_data_file": combined_csv,
        }
    # ----------------------------------------------------------------

    # --- 2) build decay chain and try to get counts safely ---
    dc = ci.DecayChain(isotope_name, A0=A0_guess, units=units)

    try:
        # IMPORTANT CHANGE: use explicit list of filenames, not 'Cu08' regex
        dc.get_counts(spectra_list, EoB=EoB, peak_data=combined_csv)
    except ValueError as e:
        msg = str(e)
        if "No objects to concatenate" in msg:
            print(f"{sample_name} – {isotope_name}: Curie found no usable counts, skipping fit.")
            return {
                "sample": sample_name,
                "isotope": isotope_name,
                "EoB": EoB,
                "units": units,
                "A0_parent": float("nan"),
                "A0_err_parent": float("nan"),
                "A0_vector": [],
                "cov_A0": [],
                "plot_file": None,
                "peak_data_file": combined_csv,
            }
        elif "does not match format '%m/%d/%Y %H:%M:%S'" in msg:
            print(f"{sample_name} – {isotope_name}: bad time format in peakData ({msg}), skipping fit.")
            return {
                "sample": sample_name,
                "isotope": isotope_name,
                "EoB": EoB,
                "units": units,
                "A0_parent": float("nan"),
                "A0_err_parent": float("nan"),
                "A0_vector": [],
                "cov_A0": [],
                "plot_file": None,
                "peak_data_file": combined_csv,
            }
        else:
            raise
    # ----------------------------------------------------------------

    # --- 3) fit A0 ---
    isotopes, A0, cov_A0 = dc.fit_A0()

    # Save a plot for this isotope & sample
    #fig = dc.plot()
    plot_name = f"{sample_name}_{isotope_name}_decay_fit.png"
    #plt.savefig(plot_name, dpi=200, bbox_inches="tight")
    #plt.close(fig)

    # EoB activity vector for the chain
    A0_list = A0.tolist() if hasattr(A0, "tolist") else [A0]
    cov_list = cov_A0.tolist() if hasattr(cov_A0, "tolist") else [[cov_A0]]

    # Parent activity and its uncertainty
    A0_parent = A0_list[0]
    var_parent = cov_list[0][0]
    err_parent = var_parent ** 0.5

    print(f"{sample_name} – {isotope_name}: A0 = {A0_parent:.3g} ± {err_parent:.3g}")

    return {
        "sample": sample_name,
        "isotope": isotope_name,
        "EoB": EoB,
        "units": units,
        "A0_parent": A0_parent,
        "A0_err_parent": err_parent,
        "A0_vector": A0_list,
        "cov_A0": cov_list,
        "plot_file": plot_name,
        "peak_data_file": combined_csv,
    }


# For alle folier og isotoper 
def main():
    # Importerer json konfigurasjoner 
    sample_conf = load_json("config_samples.json")
    isotope_conf = load_json("config_isotopes.json")

    samples = sample_conf["samples"]
    isotopes = isotope_conf["isotopes"]

    all_results = []

    # Løper gjennom folier 
    for s in samples:
        print(f"\n=== Sample {s['name']} ===")
        combined_csv = combine_peak_files_for_sample(s)

        # Løper gjennom isotoper
        for iso in isotopes:
            res = analyze_one_isotope_one_sample(s, iso, combined_csv)
            all_results.append(res)

    # Print og lag en CSV summary på EoB aktiviteter 
    df_res = pd.DataFrame(all_results)
    df_res.to_csv("EoB_activities_summary.csv", index=False)
    print("\nSaved EoB_activities_summary.csv")


if __name__ == "__main__":
    main()
