import curie as ci 
import numpy as np 

cb = ci.Calibration("Sn-foils/calibration_Det2_50cm.json")
#cb.plot()

spe = ci.Spectrum('Sn-foils/AQ09242025_Sn10_40cm_DET2.Spe')
spe.cb = cb
spe.isotopes = ['122SB', '117SNm', '114INm1', '124SB', '113SN', '119SB']
spe.plot() 

spe.summarize()