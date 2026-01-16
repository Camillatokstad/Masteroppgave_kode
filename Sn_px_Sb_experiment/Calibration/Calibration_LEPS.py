import curie as ci
import pandas as pd
import matplotlib.pyplot as plt

#Calibration LEPS 9cm 
def calibration_09cm():
    cb = ci.Calibration()

    spe_Cd109 = ci.Spectrum("DV20251105_LEPS_Cd109_09cm.Spe")
    spe_Cd109.isotopes = ['109CD']

    spe_Am241 = ci.Spectrum("DC20251030_LEPS_Am241_9cm.Spe")
    spe_Am241.isotopes = ['241AM']

    spe_Ba133 = ci.Spectrum("DP20251103_LEPS_Ba133_9cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    spe_Co57 = ci.Spectrum("DO20251103_LEPS_Co57_9cm.Spe")
    spe_Co57.isotopes = ['57CO']

    sources = [{'isotope':'109CD', 'A0':3.774E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'241AM', 'A0':3.752E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'57CO', 'A0':4.3E4, 'ref_date': '11/01/2023 13:27:02'},]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cd109, spe_Am241, spe_Ba133, spe_Co57], sources=sources)

    cb.plot() 
    cb.saveas('calibration_LEPS_09cm.json')


#Calibration LEPS 10cm 
def calibration_10cm():
    cb = ci.Calibration()

    spe_Cd109 = ci.Spectrum("DQ20251103_LEPS_Cd109_10cm.Spe")
    spe_Cd109.isotopes = ['109CD']

    spe_Am241 = ci.Spectrum("DB20251030_LEPS_Am241_10cm.Spe")
    spe_Am241.isotopes = ['241AM']

    spe_Ba133 = ci.Spectrum("DA20251030_LEPS_Ba133_10cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    spe_Co57 = ci.Spectrum("DI20251030_LEPS_Co57_10cm.Spe")
    spe_Co57.isotopes = ['57CO']

    sources = [{'isotope':'109CD', 'A0':3.774E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'241AM', 'A0':3.752E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'57CO', 'A0':4.3E4, 'ref_date': '11/01/2023 13:27:02'},]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cd109, spe_Am241, spe_Ba133, spe_Co57], sources=sources)

    cb.plot() 
    cb.saveas('calibration_LEPS_10cm.json')


#Calibration LEPS 15cm 
def calibration_15cm():
    cb = ci.Calibration()

    spe_Cd109 = ci.Spectrum("DU20251105_LEPS_Cd109_15cm.Spe")
    spe_Cd109.isotopes = ['109CD']

    spe_Am241 = ci.Spectrum("DD20251030_LEPS_Am241_15cm.Spe")
    spe_Am241.isotopes = ['241AM']

    spe_Ba133 = ci.Spectrum("CX20251029_LEPS_Ba133_15cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    spe_Co57 = ci.Spectrum("DN20251103_LEPS_Co57_15cm.Spe")
    spe_Co57.isotopes = ['57CO']

    sources = [{'isotope':'109CD', 'A0':3.774E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'241AM', 'A0':3.752E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'57CO', 'A0':4.3E4, 'ref_date': '11/01/2023 13:27:02'},]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cd109, spe_Am241, spe_Ba133, spe_Co57], sources=sources)

    cb.plot() 
    cb.saveas('calibration_LEPS_15cm.json')


#Calibration LEPS 20cm 
def calibration_20cm():
    cb = ci.Calibration()

    spe_Cd109 = ci.Spectrum("DS20251104_LEPS_Cd109_20cm.Spe")
    spe_Cd109.isotopes = ['109CD']

    spe_Am241 = ci.Spectrum("DE20251030_LEPS_Am241_20cm.Spe")
    spe_Am241.isotopes = ['241AM']

    spe_Ba133 = ci.Spectrum("CV20251029_LEPS_Ba133_20cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    spe_Co57 = ci.Spectrum("DL20251031_LEPS_Co57_20cm.Spe")
    spe_Co57.isotopes = ['57CO']

    sources = [{'isotope':'109CD', 'A0':3.774E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'241AM', 'A0':3.752E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'57CO', 'A0':4.3E4, 'ref_date': '11/01/2023 13:27:02'},]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cd109, spe_Am241, spe_Ba133, spe_Co57], sources=sources)

    cb.plot() 
    cb.saveas('calibration_LEPS_20cm.json')


#Calibration LEPS 30cm 
def calibration_30cm():
    cb = ci.Calibration()

    spe_Cd109 = ci.Spectrum("DT20251105_LEPS_Cd109_30cm.Spe")
    spe_Cd109.isotopes = ['109CD']

    spe_Am241 = ci.Spectrum("DF20251030_LEPS_Am241_30cm.Spe")
    spe_Am241.isotopes = ['241AM']

    spe_Ba133 = ci.Spectrum("CZ20251030_LEPS_Ba133_30cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    spe_Co57 = ci.Spectrum("DK20251031_LEPS_Co57_30cm.Spe")
    spe_Co57.isotopes = ['57CO']

    sources = [{'isotope':'109CD', 'A0':3.774E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'241AM', 'A0':3.752E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'57CO', 'A0':4.3E4, 'ref_date': '11/01/2023 13:27:02'},]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cd109, spe_Am241, spe_Ba133, spe_Co57], sources=sources)

    cb.plot() 
    cb.saveas('calibration_LEPS_30cm.json')


#Calibration LEPS 40cm 
def calibration_40cm():
    cb = ci.Calibration()

    spe_Cd109 = ci.Spectrum("DR20251104_LEPS_Cd109_40cm.Spe")
    spe_Cd109.isotopes = ['109CD']

    spe_Am241 = ci.Spectrum("DH20251030_LEPS_Am241_40cm.Spe")
    spe_Am241.isotopes = ['241AM']

    spe_Ba133 = ci.Spectrum("CT20251029_LEPS_Ba133_40cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    spe_Co57 = ci.Spectrum("DM20251103_LEPS_Co57_40cm.Spe")
    spe_Co57.isotopes = ['57CO']

    sources = [{'isotope':'109CD', 'A0':3.774E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'241AM', 'A0':3.752E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'57CO', 'A0':4.3E4, 'ref_date': '11/01/2023 13:27:02'},]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Cd109, spe_Am241, spe_Ba133, spe_Co57], sources=sources)

    cb.plot() 
    cb.saveas('calibration_LEPS_40cm.json')


#Calibration LEPS 60cm 
def calibration_60cm():
    cb = ci.Calibration()

   #spe_Cd109 = ci.Spectrum("DR20251104_LEPS_Cd109_40cm.Spe")
   #spe_Cd109.isotopes = ['109CD']

    spe_Am241 = ci.Spectrum("DG20251030_LEPS_Am241_60cm.Spe")
    spe_Am241.isotopes = ['241AM']

    spe_Ba133 = ci.Spectrum("CP20251028_LEPS_Ba133_60cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    spe_Co57 = ci.Spectrum("DJ20251031_LEPS_Co57_60cm.Spe")
    spe_Co57.isotopes = ['57CO']

    sources = [{'isotope':'109CD', 'A0':3.774E4, 'ref_date':'03/01/2019 12:00:00'}, 
    {'isotope':'241AM', 'A0':3.752E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'133BA', 'A0':3.859E4, 'ref_date': '03/01/2019 12:00:00'},
    {'isotope':'57CO', 'A0':4.3E4, 'ref_date': '11/01/2023 13:27:02'},]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Am241, spe_Ba133, spe_Co57], sources=sources)

    cb.plot() 
    cb.saveas('calibration_LEPS_60cm.json')



  
if __name__=='__main__':
  calibration_09cm()
  calibration_10cm()
  calibration_15cm()
  calibration_20cm()
  calibration_30cm()
  calibration_40cm()
  calibration_60cm()
  







