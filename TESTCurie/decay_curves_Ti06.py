import numpy as np 
import matplotlib.pyplot as plt 
import curie as ci
import pandas as pd
import csv


df_CC = pd.read_csv('CC220217_Ti06_18cm_50MeV_peakData.csv')
df_CO = pd.read_csv('CO020317_Ti06_18cm_50MeV_peakData.csv')

df_concat_Ti = pd.concat((df_CC,df_CO), axis=0)
df_concat_Ti.to_csv('Both_Ti06.csv')


dc = ci.DecayChain('48V', R=[[1e4,0.33]], units='h')
dc.get_counts('Ti06', EoB='02/12/2017 19:21:00', peak_data='Both_Ti06.csv')
isotopes, R, cov_R = dc.fit_R()
dc.plot() 

