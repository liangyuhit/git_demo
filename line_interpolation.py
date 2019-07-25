# -*- coding: utf-8 -*-
'''
Created on 25.07.2019

@author: yu03
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
from scipy import signal
from scipy.interpolate import interp1d

j = complex(0, 1)
c = 3e8 # 光速 [m/s]
Lamda = 633e-9 # 光波长 [m]
Fc = c / Lamda # 光频率 [Hz]

pix_size = 5.3e-6
pix_num = 1280
screen_diameter = pix_num * pix_size

x = np.linspace(0, (pix_num-1)*pix_size, pix_num)
tau0 = pix_size
fs = 1/tau0

f = 7000
phi = 0
sig = 240*np.cos(2*np.pi*f*x + phi)/2 + 240/2
window = signal.gaussian(len(sig), std=len(sig)/10)
sig = sig*window
line_noise = np.random.normal(2.43, 0.8, len(sig)) 
line_noise = line_noise.round().astype(int)
sig += line_noise

interplation_func = interp1d(x, sig, kind='cubic')
xnew = np.linspace(0, (pix_num-1)*pix_size, pix_num*10)



plt.figure(1)
plt.plot(x, sig, 'b')
# plt.plot(xnew, f(xnew), 'k')
plt.plot(xnew, interplation_func(xnew), 'r')
plt.grid(which='major', axis='both')
plt.show()