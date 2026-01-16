import curie as ci 
import numpy as np 
from pathlib import Path

cb = ci.Calibration("calibration_Det2_10cm.json")
#cb.plot()

list_job = ['GR10172025_Det2_Ni03_10cm_005.Spe', 'GR10172025_Det2_Ni03_10cm_004.Spe','GR10172025_Det2_Ni03_10cm_003.Spe',
'GR10172025_Det2_Ni03_10cm_002.Spe', 'GR10172025_Det2_Ni03_10cm_001.Spe', 'GR10172025_Det2_Ni03_10cm_000.Spe']

list_spectra = []
for job in list_job:
    spe = ci.Spectrum(job)
    spe.cb = cb
    list_spectra.append(spe)

print(list_spectra)

summed_spectrum = list_spectra[0]
for i, spec in enumerate(list_spectra[0:], start=0):
    summed_spectrum += spec
    print(f'Added spectrum {i+1}/{len(list_spectra)}')

summed_spectrum.isotopes = ["57NI","60CU","56CO","56NI",'58CO', '57CO', '55CO']

spe.isotopes = ["57NI","60CU","56CO","56NI",'58CO', '57CO', '55CO']


#spe.plot()

summed_spectrum.plot()
summed_spectrum.summarize()


this_dir = Path(__file__).resolve().parent          
dest_dir = this_dir.parent / "Decay_EoB" / "Ni"     
dest_dir.mkdir(parents=True, exist_ok=True)

out_name = dest_dir / "GR10172025_Ni03_10cm_Det2_peakData.csv"
summed_spectrum.saveas(str(out_name)) 

