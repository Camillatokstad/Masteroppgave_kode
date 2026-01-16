import curie as ci
import pandas as pd
import matplotlib.pyplot as plt

#Calibration Det2 10cm 
def calibration_10cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BA20251017_Det2_Cs137_10cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CL20251020_Det2_Eu152_10cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("BV20251017_Det2_Ba133_10cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    cb.plot() 
    cb.saveas('calibration_Det2_10cm.json')


#Calibration Det2 18cm 
def calibration_18cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BC20251017_Det2_Cs137_18cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CK20251020_Det2_Eu152_18cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe2_Eu152 = ci.Spectrum("AA20250922_Det2_Eu152_18cm.Spe")
    spe2_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("BX20251017_Det2_Ba133_18cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133, spe2_Eu152], sources=sources)

    cb.plot() 
    cb.saveas('calibration_Det2_18cm.json')


#Calibration Det2 24cm 
def calibration_24cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BD20251017_Det2_Cs137_24cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CM20251020_Det2_Eu152_24cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("BZ20251017_Det2_Ba133_24cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    cb.plot() 
    cb.saveas('calibration_Det2_24cm.json')


#Calibration Det2 30cm 
def calibration_30cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BF20251017_Det2_Cs137_30cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CR20251028_Det2_Eu152_30cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("CA20251018_Det2_Ba133_30cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    cb.plot() 
    cb.saveas('calibration_Det2_30cm.json')


#Calibration Det2 40cm 
def calibration_40cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BG20251017_Det2_Cs137_40cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CQ20251028_Det2_Eu152_40cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("CC20251018_Det2_Ba133_40cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    cb.plot() 
    cb.saveas('calibration_Det2_40cm.json')


#Calibration Det2 50cm 
def calibration_50cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BJ20251017_Det2_Cs137_50cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("AL20250923_Det2_Eu152_50cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("AD20250922_Det2_Ba133_50cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    cb.plot() 
    cb.saveas('calibration_Det2_50cm.json')


#Calibration Det2 60cm 
def calibration_60cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BL20251017_Det2_Cs137_60cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("AN20250923_Det2_Eu152_60cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("AF20250922_Det2_Ba133_60cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133], sources=sources)

    #cb.plot() 
    cb.saveas('calibration_Det2_60cm.json')


#Calibration Det2 70cm 
def calibration_70cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BM20251017_Det2_Cs137_70cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("CS20251028_Det2_Eu152_70cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe2_Eu152 = ci.Spectrum("CY20251030_Det2_Eu152_70cm.Spe")
    spe2_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("CG20251018_Det2_Ba133_70cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133, spe2_Eu152], sources=sources)

    #cb.plot() 
    cb.saveas('calibration_Det2_70cm.json')


#Calibration Det2 80cm 
def calibration_80cm():
    cb = ci.Calibration()

    spe_Cs137 = ci.Spectrum("BI20251017_Det2_Cs137_80cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    spe2_Cs137 = ci.Spectrum("CW20251029_Det2_Cs137_80cm.Spe")
    spe2_Cs137.isotopes = ['137CS']

    spe_Eu152 = ci.Spectrum("BU20251017_Det2_Eu152_80cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Ba133 = ci.Spectrum("CI20251020_Det2_Ba133_80cm_000.Spe")
    spe_Ba133.isotopes = ['133BA']

    spe2_Ba133 = ci.Spectrum("CJ20251020_Det2_Ba133_80cm_001.Spe")
    spe2_Ba133.isotopes = ['133BA']

    sources = [{'isotope':'137CS', 'A0':3.67E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'152EU', 'A0':3.822E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cs137, spe_Eu152, spe_Ba133, spe2_Cs137, spe2_Ba133], sources=sources)

    #cb.plot() 
    cb.saveas('calibration_Det2_80cm.json')

if __name__=='__main__':
  calibration_10cm()
  calibration_18cm()
  calibration_24cm()
  calibration_30cm()
  calibration_40cm()
  calibration_50cm()
  calibration_60cm()
  calibration_70cm()
  calibration_80cm()

   