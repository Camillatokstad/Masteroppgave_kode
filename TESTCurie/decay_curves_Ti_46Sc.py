import numpy as np 
import matplotlib.pyplot as plt 
import curie as ci
import pandas as pd
import csv

csv_files = [
    'Both_Ti06.csv',
    'CE230217_Ti08_18cm_50MeV_peakData.csv',
    'CF240217_Ti09_18cm_50MeV_peakData.csv',
    'CG240217_Ti10_18cm_50MeV_peakData.csv',
    'CI010317_Ti11_18cm_50MeV_peakData.csv'
]

decay_chains = {}
foil_names = ['Ti06','Ti08','Ti09','Ti10','Ti11']

for csv_file, foil_name in zip(csv_files, foil_names):
    
    df = pd.read_csv(csv_file)

    dc = ci.DecayChain('46SC', R=[[1e4, 0.33]], units='h')
    dc.get_counts(foil_name, EoB='02/12/2017 19:21:00', peak_data=csv_file)

    isotopes, R, cov_R = dc.fit_R()
    dc.plot(title=f'Decay Plot for {foil_name}')
    plt.show()
    print(dc.R)

