import curie as ci 
import numpy as np 

cb = ci.Calibration("testCurieCalib_18cm.json")
cb.plot()

spe = ci.Spectrum('BU170217_Fe01_18cm_50MeV.Spe')
spe.cb = cb
spe.isotopes = ['56CO', '57CO', '55CO', "58COm"]
spe.plot()