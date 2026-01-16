import curie as ci
import pandas as pd
import matplotlib.pyplot as plt

"""
#Calibration IDM 36cm
def calibration_36cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("Calibration/AG20250923_IDM_Cs137_36cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("Calibration/AE20250922_IDM_Eu152_36cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152], sources=sources)

    cb.plot() 
    cb.saveas('calibration_IDM_36cm.json')
  
if __name__=='__main__':
  calibration_36cm()
"""

#Calibration IDM 10cm 
def calibration_10cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("AD20251016_IDM_Cs137_10cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("AE20251016_IDM_Eu152_10cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("AI20251016_IDM_Ba133_10cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    #cb.plot() 
    cb.saveas('calibration_IDM_10cm.json')
  
if __name__=='__main__':
  calibration_10cm()



#Calibration IDM 15cm 
def calibration_15cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BP20251017_IDM_Cs137_15cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("BW20251017_IDM_Eu152_15cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("BB20251017_IDM_Ba133_15cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    #cb.plot() 
    cb.saveas('calibration_IDM_15cm.json')
  
if __name__=='__main__':
  calibration_15cm()



#Calibration IDM 20cm 
def calibration_20cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BQ20251017_IDM_Cs137_20cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("BY20251017_IDM_Eu152_20cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("BE20251017_IDM_Ba133_20cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    #cb.plot() 
    cb.saveas('calibration_IDM_20cm.json')
  
if __name__=='__main__':
  calibration_20cm()


#Calibration IDM 25cm 
def calibration_25cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BR20251017_IDM_Cs137_25cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CB20251018_IDM_Eu152_25cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("BH20251017_IDM_Ba133_25cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    #cb.plot() 
    cb.saveas('calibration_IDM_25cm.json')
  
if __name__=='__main__':
  calibration_25cm()



#Calibration IDM 30cm 
def calibration_30cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("AK20250923_IDM_Cs137_30cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CD20251018_IDM_Eu152_30cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("AB20250922_IDM_Ba133_30cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    #cb.plot() 
    cb.saveas('calibration_IDM_30cm.json')
  
if __name__=='__main__':
  calibration_30cm()



#Calibration IDM 40cm 
def calibration_40cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("AI20250923_IDM_Cs137_40cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CF20251018_IDM_Eu152_40cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("BO20251017_IDM_Ba133_40cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    #cb.plot() 
    cb.saveas('calibration_IDM_40cm.json')
  
if __name__=='__main__':
  calibration_40cm()



#Calibration IDM 45cm 
def calibration_45cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BS20251017_IDM_Cs137_45cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CO20251028_IDM_Eu152_45cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("BN20251017_IDM_Ba133_45cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Ba133], sources=sources)

    #cb.plot() 
    cb.saveas('calibration_IDM_45cm.json')
  
if __name__=='__main__':
  calibration_45cm()


#Calibration IDM 52cm 
def calibration_52cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BT20251017_IDM_Cs137_52cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CH20251020_IDM_Eu152_52cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("BK20251017_IDM_Ba133_52cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    cb.plot() 
    cb.saveas('calibration_IDM_52cm.json')
  
if __name__=='__main__':
  calibration_52cm()






   