import numpy as np 
import matplotlib.pyplot as plt 
import curie as ci
import pandas as pd
import csv

df_AE = pd.read_csv('AE09232025_Cu12_52cm_IDM_peakData.csv')
df_AL = pd.read_csv('AL09232025_Cu12_40cm_IDM_peakData.csv')
df_BN = pd.read_csv('BN09242025_Cu12_25cm_IDM_peakData.csv')
df_DS = pd.read_csv('DS09252025_Cu12_10cm_IDM_peakData.csv')
df_EV = pd.read_csv('EV09272025_Cu12_10cm_IDM_peakData.csv')
df_EV = pd.read_csv('EV09272025_Cu12_10cm_IDM_peakData.csv')
df_GM = pd.read_csv('GM10182025_IDM_Cu12_10cm_job_peakData.csv')


df_concat = pd.concat((df_AE, df_AL, df_BN, df_DS, df_EV, df_GM), axis=0)
df_concat.to_csv('Cu12_IDM_peakData.csv')

dc = ci.DecayChain('56CO', R=[[5,1]], units='h')
dc.get_counts('Cu12', EoB='09/23/2025 18:35:00', peak_data='Cu12_IDM_peakData.csv')
isotopes, R, cov_R = dc.fit_R()
dc.plot() 
plt.show()