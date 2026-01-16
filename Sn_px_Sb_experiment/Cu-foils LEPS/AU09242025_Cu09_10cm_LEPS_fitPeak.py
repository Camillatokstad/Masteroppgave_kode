import curie as ci 
import numpy as np 
from pathlib import Path

cb = ci.Calibration("/Users/camillatokstad/Documents/FA/Masteroppgave/Sn(p,x)Sb_experiment/Cu-foils LEPS/calibration_LEPS_10cm.json")
#cb.plot()

spe = ci.Spectrum('/Users/camillatokstad/Documents/FA/Masteroppgave/Sn(p,x)Sb_experiment/Cu-foils LEPS/AU09242025_Cu09_10cm_LEPS.Spe')
spe.cb = cb
spe.isotopes = ['63ZN', '58COm',
 '62ZN', '65ZN', '56CO']
spe.plot(fit=False)
#spe.plot()

this_dir = Path(__file__).resolve().parent          
dest_dir = this_dir.parent / "Decay_EoB" / "Cu"     
dest_dir.mkdir(parents=True, exist_ok=True)

out_name = dest_dir / "AU09242025_Cu09_10cm_LEPS_peakData.csv"
spe.saveas(str(out_name))