import curie as ci 
import numpy as np 

cb = ci.Calibration("testCurieCalib_18cm.json")
cb.plot()

spe = ci.Spectrum('CF240217_Ti09_18cm_50MeV.Spe')
spe.cb = cb
spe.isotopes = ['48V', '47V', '49V', "52V", '53V','45TI', '44TI', '46V', '46SC', '47SC', "48SC", '49SC', '41CA', '45CA', '47CA', '42K', '43K','44K','45K','46K', '51TI', '44SCm']
spe.plot()
spe.saveas('CF240217_Ti09_18cm_50MeV_peakData.csv')