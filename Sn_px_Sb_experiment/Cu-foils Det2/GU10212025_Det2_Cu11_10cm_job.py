
import curie as ci 
import numpy as np 
from pathlib import Path

cb = ci.Calibration("calibration_Det2_10cm.json")
#cb.plot()

list_job = ['GU10212025_Det2_Cu11_10cm_000.Spe', 'GU10212025_Det2_Cu11_10cm_001.Spe']

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

summed_spectrum.isotopes = ['62CU', '60CU', '63ZN', '61CO', '61CU', '58COm',
 '62ZN', '64CU', '58CO', '65ZN', '56CO', '57CO', '64ZN', 
 '62NI', '60NI', '61NI', '59NI', '57NI', '56NI', '54MN', '60CO', '69ZNm', '66GA']

spe.isotopes = ['62CU', '60CU', '63ZN', '61CO', '61CU', '58COm',
 '62ZN', '64CU', '58CO', '65ZN', '56CO', '57CO', '64ZN', 
 '62NI', '60NI', '61NI', '59NI', '57NI', '56NI', '54MN', '60CO', '69ZNm', '66GA']


#spe.plot()
summed_spectrum.plot()
summed_spectrum.summarize()
#print(summed_spectrum)
#summed_spectrum.saveas('GM10182025_IDM_Cu12_10cm_job_peakData.csv')

this_dir = Path(__file__).resolve().parent          
dest_dir = this_dir.parent / "Decay_EoB" / "Cu"     
dest_dir.mkdir(parents=True, exist_ok=True)

out_name = dest_dir / "GU10212025_Cu12_10cm_Det2_peakData.csv"
summed_spectrum.saveas(str(out_name)) 

