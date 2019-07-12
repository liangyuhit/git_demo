# -*- coding: utf-8 -*-
'''
Created on 11.07.2019

@author: yu03
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
from scipy import signal
duration = 1.0
fs = 400.0
samples = int(fs*duration)
t = np.arange(samples) / fs

signal = (chirp(t, 20.0, t[-1], 20.0)+1)*signal.gaussian(len(t), std=len(t)/10)
signal += np.random.normal(0, 0.1, len(signal))
signal_diff = np.diff(signal)
# signal *= (1.0 + 0.5 * np.sin(2.0*np.pi*0.5*t))
analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)
plt.plot(signal, label='signal')
plt.plot(signal_diff, label='signal')
# plt.plot(t[1:], amplitude_envelope, label='envelope')
plt.show()
