# -*- coding: utf-8 -*-
'''
Created on 07.08.2019

@author: yu03
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

f = 1e2
N = 1e4
fs = 1e4
x = np.arange(N)/fs
t = N/fs
print('Points number: ', N)
print('fs: ', fs, 'Hz')
print('time: ', t, 's')

sig = np.cos(2*np.pi*f*x)
noise = np.random.rand(len(x))/10
sig += noise

f_line, PS = signal.welch(sig, fs, nperseg=1024)
PSD = np.sqrt(PS)
plt.figure('Signal')
plt.plot(x,sig)
plt.xlabel('sample')
plt.ylabel('Amplitude [V]')
plt.grid(which='major', axis='both')

plt.figure('PSD')
plt.loglog(f_line, PSD)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V/sqrt(Hz)]')
plt.grid(which='major', axis='both')
plt.show()