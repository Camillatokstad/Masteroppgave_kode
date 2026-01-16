import numpy as np 
import matplotlib.pyplot as plt 
import curie as ci
import pandas as pd
import csv

df_AC = pd.read_csv('AC09232025_Cu10_52cm_IDM_peakData.csv')
df_AJ = pd.read_csv('AJ09232025_Cu10_45cm_IDM_peakData.csv')
df_BL = pd.read_csv('BL09242025_Cu10_30cm_IDM_peakData.csv')
df_DU = pd.read_csv('DU09252025_Cu10_10cm_IDM_peakData.csv')
df_EX = pd.read_csv('EX09272025_Cu10_10cm_IDM_peakData.csv')
df_GN = pd.read_csv('GN10212025_IDM_Cu10_10cm_job_peakData.csv')


df_concat = pd.concat((df_AC, df_AJ, df_BL, df_DU, df_EX, df_GN), axis=0)
df_concat.to_csv('Cu10_IDM_peakData.csv')

dc = ci.DecayChain('62ZN', A0=1e4, units='h')
dc.get_counts('Cu10', EoB='09/23/2025 18:35:00', peak_data='Cu10_IDM_peakData.csv')
isotopes, A0, cov_A0 = dc.fit_A0()
dc.plot()  
print(A0, cov_A0) 
plt.show() 