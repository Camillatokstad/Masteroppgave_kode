import curie as ci 
import numpy as np 

cb = ci.Calibration("calibration_IDM_10cm.json")
#cb.plot()

spe = ci.Spectrum('EW09272025_Cu11_10cm_IDM.Spe')
spe.cb = cb
spe.isotopes = ['62CU', '60CU', '63ZN', '61CO', '61CU', '58COm',
 '62ZN', '64CU', '58CO', '65ZN', '56CO', '57CO', '64ZN', 
 '62NI', '60NI', '61NI', '59NI', '57NI', '56NI', '54MN', '60CO', '69ZNm', '66GA'  ]
spe.plot() 

spe.summarize()

spe.saveas('EW09272025_Cu11_10cm_IDM_peakData.csv') 