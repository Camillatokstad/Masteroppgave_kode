import pandas as pd

excel_file = "/Users/camillatokstad/Documents/FA/Masteroppgave/Uncertainties_foil_measurements/foils_measurements.xlsx"
csv_file = "/Users/camillatokstad/Documents/FA/Masteroppgave/Uncertainties_foil_measurements/foils_measurements_Cu.csv"

# Read only the 'Cu' sheet
df = pd.read_excel(excel_file, sheet_name='Cu')

# Save as CSV
df.to_csv(csv_file, index=False)

print(f"Converted Excel sheet 'Cu' to: {csv_file}")