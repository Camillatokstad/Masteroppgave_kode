import curie as ci 
import numpy as np 

cb = ci.Calibration("Sn-foils/calibration_Det2_50cm.json")
#cb.plot()

spe = ci.Spectrum('Sn-foils/FT09302025_Det2_Sn02_10cm_007.Spe')
spe.cb = cb
spe.isotopes = ['122SB', '117SNm', '114INm1', '124SB', '113SN']
spe.plot() 

spe.summarize()