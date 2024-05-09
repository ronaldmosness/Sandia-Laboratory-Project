# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:51:21 2024

@author: PC
"""

import scipy
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
degraded_data1 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_degraded/eegd9.csv', header=None)
degraded_data1 = np.transpose(degraded_data1)
raw_data1 = np.array((degraded_data1))
fs = 1000
wl = fs*4
pwelch1 = signal.welch(raw_data1,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
dsig1 = pwelch1[1]

np.savetxt('degraded_w9.csv', dsig1, delimiter=',')

degraded_data2 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_degraded/eegd10.csv', header=None)
degraded_data2 = np.transpose(degraded_data2)
raw_data2 = np.array((degraded_data2))
fs = 1000
wl = fs*4
pwelch2 = signal.welch(raw_data2,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
dsig2 = pwelch2[1]

np.savetxt('degraded_w10.csv', dsig2, delimiter=',')

degraded_data3 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_degraded/eegd11.csv', header=None)
degraded_data3 = np.transpose(degraded_data3)
raw_data3 = np.array((degraded_data3))
fs = 1000
wl = fs*4
pwelch3 = signal.welch(raw_data3,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
dsig3 = pwelch3[1]

np.savetxt('degraded_w11.csv', dsig3, delimiter=',')

degraded_data4 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_degraded/eegd12.csv', header=None)
degraded_data4 = np.transpose(degraded_data4)
raw_data4 = np.array((degraded_data4))
fs = 1000
wl = fs*4
pwelch4 = signal.welch(raw_data4,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
dsig4 = pwelch4[1]

np.savetxt('degraded_w12.csv', dsig4, delimiter=',')

degraded_data5 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_degraded/eegd13.csv', header=None)
degraded_data5 = np.transpose(degraded_data5)
raw_data5 = np.array((degraded_data5))
fs = 1000
wl = fs*4
pwelch5 = signal.welch(raw_data5,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
dsig5 = pwelch5[1]

np.savetxt('degraded_w13.csv', dsig5, delimiter=',')

degraded_data6 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_degraded/eegd14.csv', header=None)
degraded_data6 = np.transpose(degraded_data6)
raw_data6 = np.array((degraded_data6))
fs = 1000
wl = fs*4
pwelch6 = signal.welch(raw_data6,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
dsig6 = pwelch6[1]

np.savetxt('degraded_w14.csv', dsig6, delimiter=',')

degraded_data7 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_degraded/eegd15.csv', header=None)
degraded_data7 = np.transpose(degraded_data7)
raw_data7 = np.array((degraded_data7))
fs = 1000
wl = fs*4
pwelch7 = signal.welch(raw_data7,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
dsig7 = pwelch7[1]

np.savetxt('degraded_w15.csv', dsig7, delimiter=',')

degraded_data8 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_degraded/eegd16.csv', header=None)
degraded_data8 = np.transpose(degraded_data8)
raw_data8 = np.array((degraded_data8))
fs = 1000
wl = fs*4
pwelch8 = signal.welch(raw_data8,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
dsig8 = pwelch8[1]

np.savetxt('degraded_w16.csv', dsig8, delimiter=',')

degraded_data9 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_degraded/eegd17.csv', header=None)
degraded_data9 = np.transpose(degraded_data9)
raw_data9 = np.array((degraded_data9))
fs = 1000
wl = fs*4
pwelch9 = signal.welch(raw_data9,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
dsig9 = pwelch9[1]

np.savetxt('degraded_w17.csv', dsig9, delimiter=',')

degraded_data10 = pd.read_csv(r'C:/Users/PC/Desktop/sandra/data_degraded/eegd18.csv', header=None)
degraded_data10 = np.transpose(degraded_data10)
raw_data10 = np.array((degraded_data10))
fs = 1000
wl = fs*4
pwelch10 = signal.welch(raw_data10,fs=1000,window='hann',nperseg=wl,noverlap=wl*0.5,nfft=wl)
dsig10 = pwelch10[1]

np.savetxt('degraded_w18.csv', dsig10, delimiter=',')




