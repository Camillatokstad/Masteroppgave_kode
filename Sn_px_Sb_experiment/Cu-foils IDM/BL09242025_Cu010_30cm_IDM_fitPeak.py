import curie as ci 
import numpy as np 
from pathlib import Path

cb = ci.Calibration("calibration_IDM_30cm.json")
#cb.plot()

spe = ci.Spectrum('BL09242025_Cu10_30cm_IDM.Spe')
spe.cb = cb
spe.isotopes = ['62CU', '60CU', '63ZN', '61CO', '61CU', '58COm',
 '62ZN', '64CU', '58CO', '65ZN', '56CO', '57CO', '64ZN', 
 '62NI', '60NI', '61NI', '59NI', '57NI', '56NI', '54MN', '60CO', '69ZNm', '66GA' ]
spe.plot() 

this_dir = Path(__file__).resolve().parent          
dest_dir = this_dir.parent / "Decay_EoB" / "Cu"     
dest_dir.mkdir(parents=True, exist_ok=True)

out_name = dest_dir / "BL09242025_Cu10_30cm_IDM_peakData.csv"
spe.saveas(str(out_name))