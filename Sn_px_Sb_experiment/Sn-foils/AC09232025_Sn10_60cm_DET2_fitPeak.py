import curie as ci 
import numpy as np 

cb = ci.Calibration("Sn-foils/calibration_Det2_50cm.json")
#cb.plot()

spe = ci.Spectrum('Sn-foils/AC09232025_Sn10_60cm_DET2.Spe')
spe.cb = cb
spe.isotopes = ['122SB', '117SNm', '114INm1', '124SB', '113SN', '119SB']
spe.plot() 

spe.summarize()