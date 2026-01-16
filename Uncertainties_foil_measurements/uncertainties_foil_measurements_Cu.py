import math
import statistics
import pandas as pd

resolutions = {
    "length": 0.01,      # mm 
    "width": 0.01,       # mm
    "thickness": 0.001   # mm
    #"mass": 
}
k = 2
filename =  "/Users/camillatokstad/Documents/FA/Masteroppgave/Uncertainties_foil_measurements/foils_measurements.xlsx"
 
sheet = 0                 

df = pd.read_excel(filename, sheet_name='Cu')

length_cols = [col for col in df.columns if col.lower().startswith("Length (mm)")]
width_cols = [col for col in df.columns if col.lower().startswith("Width (mm)")]
thickness_cols = [col for col in df.columns if col.lower().startswith("Thickness (mm)")]

def compute_uncertainty(values, resolution):
    """Return mean and expanded uncertainty U (k=2)."""
    vals = [v for v in values if pd.notna(v)]
    if len(vals) == 0:
        return None, None
    mean = statistics.mean(vals)
    s = statistics.stdev(vals) if len(vals) > 1 else 0.0
    uA = s / math.sqrt(len(vals)) if len(vals) > 1 else 0.0
    uB = resolution / math.sqrt(12)
    uc = math.sqrt(uA**2 + uB**2)
    U = k * uc
    return mean, U

df["Length_mean"], df["Length_U"] = zip(*df[length_cols].apply(lambda row: compute_uncertainty(row.values, resolutions["length"]), axis=1))
df["Width_mean"], df["Width_U"] = zip(*df[width_cols].apply(lambda row: compute_uncertainty(row.values, resolutions["width"]), axis=1))
df["Thickness_mean"], df["Thickness_U"] = zip(*df[thickness_cols].apply(lambda row: compute_uncertainty(row.values, resolutions["thickness"]), axis=1))

df.to_excel("foil_results.xlsx", index=False)
print("Results saved to foil_results.xlsx")
