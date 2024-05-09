# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:13:34 2024

@author: PC
"""

import scipy
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
healthy_data1 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_healthy/eegh9.csv', header=None)
healthy_data1 = np.transpose(healthy_data1)
raw_data1 = np.array((healthy_data1))
fs = 1000
wl = fs*4
pwelch1 = signal.welch(raw_data1,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
hsig1 = pwelch1[1]

np.savetxt('healthy_w9.csv', hsig1, delimiter=',')

healthy_data2 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_healthy/eegh10.csv', header=None)
healthy_data2 = np.transpose(healthy_data2)
raw_data2 = np.array((healthy_data2))
fs = 1000
wl = fs*4
pwelch2 = signal.welch(raw_data2,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
hsig2 = pwelch2[1]

np.savetxt('healthy_w10.csv', hsig2, delimiter=',')

healthy_data3 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_healthy/eegh11.csv', header=None)
healthy_data3 = np.transpose(healthy_data3)
raw_data3 = np.array((healthy_data3))
fs = 1000
wl = fs*4
pwelch3 = signal.welch(raw_data3,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
hsig3 = pwelch3[1]

np.savetxt('healthy_w11.csv', hsig3, delimiter=',')

healthy_data4 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_healthy/eegh12.csv', header=None)
healthy_data4 = np.transpose(healthy_data4)
raw_data4 = np.array((healthy_data4))
fs = 1000
wl = fs*4
pwelch4 = signal.welch(raw_data4,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
hsig4 = pwelch4[1]

np.savetxt('healthy_w12.csv', hsig4, delimiter=',')

healthy_data5 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_healthy/eegh13.csv', header=None)
healthy_data5 = np.transpose(healthy_data5)
raw_data5 = np.array((healthy_data5))
fs = 1000
wl = fs*4
pwelch5 = signal.welch(raw_data5,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
hsig5 = pwelch5[1]

np.savetxt('healthy_w13.csv', hsig5, delimiter=',')

healthy_data6 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_healthy/eegh14.csv', header=None)
healthy_data6 = np.transpose(healthy_data6)
raw_data6 = np.array((healthy_data6))
fs = 1000
wl = fs*4
pwelch6 = signal.welch(raw_data6,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
hsig6 = pwelch6[1]

np.savetxt('healthy_w14.csv', hsig6, delimiter=',')

healthy_data7 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_healthy/eegh15.csv', header=None)
healthy_data7 = np.transpose(healthy_data7)
raw_data7 = np.array((healthy_data7))
fs = 1000
wl = fs*4
pwelch7 = signal.welch(raw_data7,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
hsig7 = pwelch7[1]

np.savetxt('healthy_w15.csv', hsig7, delimiter=',')

healthy_data8 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_healthy/eegh16.csv', header=None)
healthy_data8 = np.transpose(healthy_data8)
raw_data8 = np.array((healthy_data8))
fs = 1000
wl = fs*4
pwelch8 = signal.welch(raw_data8,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
hsig8 = pwelch8[1]

np.savetxt('healthy_w16.csv', hsig8, delimiter=',')

healthy_data9 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_healthy/eegh17.csv', header=None)
healthy_data9 = np.transpose(healthy_data9)
raw_data9 = np.array((healthy_data9))
fs = 1000
wl = fs*4
pwelch9 = signal.welch(raw_data9,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
hsig9 = pwelch9[1]

np.savetxt('healthy_w17.csv', hsig9, delimiter=',')

healthy_data10 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_healthy/eegh18.csv', header=None)
healthy_data10 = np.transpose(healthy_data10)
raw_data10 = np.array((healthy_data10))
fs = 1000
wl = fs*4
pwelch10 = signal.welch(raw_data10,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
hsig10 = pwelch10[1]

np.savetxt('healthy_w18.csv', hsig10, delimiter=',')





