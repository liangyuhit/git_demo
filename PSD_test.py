# -*- coding: utf-8 -*-
'''
Created on 07.08.2019

@author: yu03
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

f1, f2, f3 = 50, 100, 200
A1, A2, A3 = 0.1, 1, 10
phi1, phi2, phi3 = 0, 1, 2
N = 10000
fs = 1e4
x = np.arange(N)/fs
t = N/fs
print('Points number: ', N)
print('fs: ', fs, 'Hz')
print('time: ', t, 's')

sig = A1*np.cos(2*np.pi*f1*x+phi1) + A2*np.cos(2*np.pi*f2*x+phi2) + A3*np.cos(2*np.pi*f3*x+phi3)
noise = np.random.rand(len(x))/10
sig += noise

f_line, PS = signal.welch(sig, fs, nperseg=len(sig))
PSD = np.sqrt(PS)

# plt.figure('Signal')
# plt.plot(sig)
# plt.xlabel('sample')
# plt.ylabel('Amplitude [V]')
# plt.grid(which='major', axis='both')

plt.figure('PSD')
plt.loglog(f_line, PSD)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V/sqrt(Hz)]')
plt.grid(which='major', axis='both')
plt.show()