import numpy as np 
import matplotlib.pyplot as plt 
import curie as ci
import pandas as pd
import csv
"""
csv_files = [
    'AB09232025_Cu09_52cm_IDM_peakData.csv',
    'AI09232025_Cu09_45cm_IDM_peakData.csv',
    'BK09242025_Cu09_30cm_IDM_peakData.csv',
    'DV09252025_Cu09_10cm_IDM_peakData.csv',
    'EY09272025_Cu09_10cm_IDM_peakData.csv'
]

decay_chains = {}
foil_names = ['Cu09']

for csv_file, foil_name in zip(csv_files, foil_names):
    
    df = pd.read_csv(csv_file)

    dc = ci.DecayChain('62ZN', R=[[5,1]], units='h')
    dc.get_counts(foil_name, EoB='09/23/2025 18:35:00', peak_data=csv_file)

    isotopes, R, cov_R = dc.fit_R()
    dc.plot(title=f'Decay Plot for {foil_name}')
    plt.show()
    print(dc.R)
"""


df_AB = pd.read_csv('AB09232025_Cu09_52cm_IDM_peakData.csv')
df_AI = pd.read_csv('AI09232025_Cu09_45cm_IDM_peakData.csv')
df_BK = pd.read_csv('BK09242025_Cu09_30cm_IDM_peakData.csv')
df_DV = pd.read_csv('DV09252025_Cu09_10cm_IDM_peakData.csv')
df_EY = pd.read_csv('EY09272025_Cu09_10cm_IDM_peakData.csv')

df_concat = pd.concat((df_AB, df_AI, df_BK, df_DV, df_EY), axis=0)
df_concat.to_csv('Cu09_IDM_peakData.csv')

dc = ci.DecayChain('62ZN', R=[[5,1]], units='h')
dc.get_counts('Cu09', EoB='09/23/2025 18:35:00', peak_data='Cu09_IDM_peakData.csv')
isotopes, R, cov_R = dc.fit_R()
dc.plot() 
plt.show()


