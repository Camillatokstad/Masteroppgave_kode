import curie as ci 
import numpy as np 

cb = ci.Calibration("calibrationByHand_CK010317_Ti02_18cm_30MeV.json")
#cb.plot()

spe = ci.Spectrum('CI010317_Ti11_18cm_50MeV.Spe')
spe.cb = cb
spe.isotopes = ['48V', '47V', '49V', "52V", '53V','45TI', '44TI', '46V', '46SC', '47SC', "48SC", '49SC', '41CA', '45CA', '47CA', '42K', '43K','44K','45K','46K', '51TI', '44SCm']
spe.plot()
spe.saveas('CI010317_Ti11_18cm_50MeV_peakData.csv')