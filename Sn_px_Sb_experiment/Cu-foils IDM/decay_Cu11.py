import numpy as np 
import matplotlib.pyplot as plt 
import curie as ci
import pandas as pd
import csv

df_AD = pd.read_csv('AD09232025_Cu11_45cm_IDM_peakData.csv')
df_AK = pd.read_csv('AK09232025_Cu11_40cm_IDM_peakData.csv')
df_BM = pd.read_csv('BM09242025_Cu11_30cm_IDM_peakData.csv')
df_DT = pd.read_csv('DT09252025_Cu11_10cm_IDM_peakData.csv')
df_EW = pd.read_csv('EW09272025_Cu11_10cm_IDM_peakData.csv')


df_concat = pd.concat((df_AD, df_AK, df_BM, df_DT, df_EW), axis=0)
df_concat.to_csv('Cu11_IDM_peakData.csv')

dc = ci.DecayChain('62ZN', R=[[5,1]], units='h')
dc.get_counts('Cu11', EoB='09/23/2025 18:35:00', peak_data='Cu11_IDM_peakData.csv')
isotopes, R, cov_R = dc.fit_R()
dc.plot() 
plt.show()