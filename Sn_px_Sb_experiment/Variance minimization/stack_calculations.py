import numpy as np
import curie as ci
import pandas as pd

x_kapton = 0.013
x_silicone = 0.013
ad_degrader_a = 599. #2.24 mm
ad_degrader_b = 415.0 #1.55 mm
ad_degrader_c = 261.5 #0.97 mm
# ad_degrader_d = 599.0
ad_degrader_e = 68.3 #0.256 mm
ad_degrader_h = 33.8
ad_be_backing = 4.425 #23.9130435 microns



#change thickness in 't' with area density 
def stack_55(E_p):
    stack = [
    #compartment01
    {'compound':'Ni', 'name':'Ni01', 'ad':23.079},
    {'compound':'Sn', 'name':'Sn01', 'ad':37.475},
    {'compound':'Ta', 'name':'Ta01', 'ad':27.334},
    {'compound':'Cu', 'name':'Cu01', 'ad':21.906},
    {'compound':'Al', 'name':'Al_degrader_A1', 'ad':ad_degrader_a},
    # compartment02
    {'compound':'Ni', 'name':'Ni02', 'ad':23.091},
    {'compound':'Sn', 'name':'Sn02', 'ad':37.211},
    {'compound':'Ta', 'name':'Ta02', 'ad':27.396},
    {'compound':'Cu', 'name':'Cu02', 'ad':22.235},
    {'compound':'Al', 'name':'Al_degrader_B2', 'ad':ad_degrader_b},
    # compartment03
    {'compound':'Ni', 'name':'Ni03', 'ad':22.966},
    {'compound':'Sn', 'name':'Sn03', 'ad':37.130},
    {'compound':'Ta', 'name':'Ta03', 'ad':27.702},
    {'compound':'Cu', 'name':'Cu03', 'ad':22.253},
    {'compound':'Al', 'name':'Al_degrader_C5', 'ad':ad_degrader_c},
    # compartment04
    {'compound':'Ni', 'name':'Ni04', 'ad':22.982},
    {'compound':'Sn', 'name':'Sn04', 'ad':36.990},
    {'compound':'Ta', 'name':'Ta04', 'ad':27.518},
    {'compound':'Cu', 'name':'Cu04', 'ad':22.289},
    {'compound':'Al', 'name':'Al_degrader_E8_E1', 'ad':2*ad_degrader_e},
    # compartment05
    {'compound':'Ni', 'name':'Ni05', 'ad':22.942},
    {'compound':'Sn', 'name':'Sn05', 'ad':8.004},
    {'compound':'Ta', 'name':'Ta05', 'ad':27.197},
    {'compound':'Cu', 'name':'Cu05', 'ad':22.311},
    {'compound':'Al', 'name':'Al_degrader_E4_E3_E2', 'ad':3*ad_degrader_e},
    # compartment06
    {'compound':'Ni', 'name':'Ni06', 'ad':22.631},
    {'compound':'Sn', 'name':'Sn06', 'ad':7.816},
    {'compound':'Ta', 'name':'Ta06', 'ad':27.374},
    {'compound':'Cu', 'name':'Cu06', 'ad':22.233},
    {'compound':'Al', 'name':'Al_degrader_E7_E6_E5', 'ad':3*ad_degrader_e},
    # compartment07
    {'compound':'Ni', 'name':'Ni07', 'ad':22.529},
    {'compound':'Sn', 'name':'Sn07', 'ad':7.917},
    {'compound':'Ta', 'name':'Ta07', 'ad':27.539},
    {'compound':'Cu', 'name':'Cu07', 'ad':22.258},
]
    full_stack = ci.Stack(stack, E0=E_p, particle='p', dE0=0.55, N=1E4, max_steps=100)
    return full_stack

def stack_30(E_p):
    stack = [
    #compartment08
    {'compound':'Ni', 'name':'Ni08', 'ad':23.145},
    {'compound':'Sn', 'name':'Sn08', 'ad':8.047},
    {'compound':'Ta', 'name':'Ta08', 'ad':27.227},
    {'compound':'Cu', 'name':'Cu08', 'ad':22.197},
    {'compound':'Al', 'name':'Al_degrader_E2_E1', 'ad':2*ad_degrader_e},
    # compartment09
    {'compound':'Ni', 'name':'Ni09', 'ad':22.662},
    {'compound':'Sn', 'name':'Sn09', 'ad':7.829},
    {'compound':'Ta', 'name':'Ta09', 'ad':27.337},
    {'compound':'Cu', 'name':'Cu09', 'ad':22.091},
    {'compound':'Al', 'name':'Al_degrader_E4_E3', 'ad':2*ad_degrader_e},
    # compartment10
    {'compound':'Ni', 'name':'Ni10', 'ad':23.107},
    {'compound':'Sn', 'name':'Sn10', 'ad':8.232},
    {'compound':'Ta', 'name':'Ta10', 'ad':27.165},
    {'compound':'Cu', 'name':'Cu10', 'ad':22.259},
    {'compound':'Al', 'name':'Al_degrader_E6_E5', 'ad':2*ad_degrader_e},
    # compartment11
    {'compound':'Ni', 'name':'Ni11', 'ad':22.941},
    {'compound':'Sn', 'name':'Sn11', 'ad':7.982},
    {'compound':'Ta', 'name':'Ta11', 'ad':27.200},
    {'compound':'Cu', 'name':'Cu11', 'ad':22.211},
    {'compound':'Al', 'name':'Al_degrader_E8_E7', 'ad':2*ad_degrader_e},
    # compartment12
    {'compound':'Ni', 'name':'Ni12', 'ad':23.155},
    {'compound':'Sn', 'name':'Sn12', 'ad':8.021},
    {'compound':'Ta', 'name':'Ta12', 'ad':27.702},
    {'compound':'Cu', 'name':'Cu12', 'ad':22.177},
    {'compound':'Al', 'name':'Al_degrader_E9', 'ad':ad_degrader_e},
    # compartment13
    {'compound':'Ni', 'name':'Ni13', 'ad':23.153},
    {'compound':'Sn', 'name':'Sn13', 'ad':7.354},
    {'compound':'Ta', 'name':'Ta13', 'ad':27.337},
    {'compound':'Cu', 'name':'Cu13', 'ad':22.168},
    {'compound':'Al', 'name':'Al_degrader_E10', 'ad':ad_degrader_e},
    # compartment14
    {'compound':'Ni', 'name':'Ni14', 'ad':23.067},
    {'compound':'Sn', 'name':'Sn14', 'ad':7.620},
    {'compound':'Ta', 'name':'Ta14', 'ad':27.361},
    {'compound':'Cu', 'name':'Cu14', 'ad':22.125},
    # {'compound':'Al', 'name':'Al_degrader_E14', 'ad':ad_degrader_e},
    ]
    full_stack = ci.Stack(stack, E0=E_p, particle='p', dE0=0.55, N=1E4, max_steps=100)
    return full_stack

st =ci.Stack(stack_30, E0=30, dE0=0.45, N =1e6, particle='p', dp=1)
st.saveas('stack_30MeV_dp_1.csv')
st.plot()