import curie as ci
import pandas as pd
import matplotlib.pyplot as plt


def calibration_18cm():
    cb = ci.Calibration()

    spe_Ba133 = ci.Spectrum("./Ba133_150217_18cm.Spe")
    spe_Ba133.isotopes = ['133BA']
    #spe_Ba133.plot()
    spe_Eu152 = ci.Spectrum("./Eu152_150217_18cm.Spe")
    spe_Eu152.isotopes = ['152EU']

    spe_Co56 = ci.Spectrum("./Co56_190217_18cm.Spe")
    spe_Co56.isotopes = ['56CO']

    spe_Cs137 = ci.Spectrum("./Cs137_240217_18cm.Spe")
    spe_Cs137.isotopes = ['137CS']

    sources = [{'isotope':'133BA', 'A0':3.989e4, 'ref_date': '01/01/2009 12:00:00'},
     {'isotope':'152EU', 'A0':370000, 'ref_date': '11/01/1984 12:00:00'},
      {'isotope':'56CO', 'A0':3.929e4, 'ref_date': '01/01/2009 12:00:00'},
      {'isotope':'137CS', 'A0':3.855E4, 'ref_date':'01/01/2009 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([spe_Ba133, spe_Eu152, spe_Co56], sources=sources)

    cb.plot() 
    cb.saveas('testCurieCalib_18cm.json')


def calibration_18cm_new():

    cb = ci.Calibration()

    spe_Ba133 = ci.Spectrum("./Ba133_150217_18cm.Spe")
    spe_Ba133.isotopes = ['133BA']

    spe_Co56 = ci.Spectrum("./Co56_190217_18cm.Spe")
    spe_Co56.isotopes = ['56CO']

    sp_newCs137 = ci.Spectrum('./newCs137_030317_18cm.Spe')
    sp_newCs137.isotopes = ['137CS'] 

    sp_newEu152 = ci.Spectrum('./newEu152_030317_18cm.Spe')
    sp_newEu152.isotopes = ['152EU'] 

    sources = [{'isotope':'137CS', 'A0':3.855E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'152EU', 'A0':370000, 'ref_date':'11/01/1984 12:00:00'},
               {'isotope':'133BA', 'A0':3.989e4, 'ref_date': '01/01/2009 12:00:00'},
               {'isotope':'56CO', 'A0':3.929e4, 'ref_date': '01/01/2009 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_newCs137, sp_newEu152], sources=sources)
    cb.plot()
    cb.saveas('testCurieCalib_18cm_new.json')
  

if __name__=='__main__':
  calibration_18cm()
  calibration_18cm_new()
   