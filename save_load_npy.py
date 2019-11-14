# -*- coding: utf-8 -*-
'''
Created on 31.07.2019

@author: yu03
'''
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fit_func_line(x, p, q):
    return p*x+q


file_name = r'F:\Data_Liang_Yu\Users\yu03\Desktop\3-DoF Interferometer\Experiment Record\!!! Isolation Room Test\Upstair well alighned\20190808 nonliearity test\Black Head\Noise\New Isolation\openmode_weight_2.npy'


if 0:
    for i in range(100):
        a = np.zeros(3)
        b = np.random.randint(0,5,3)
        c = 100
        out = np.array([a,b,c])
        print(out)
        f = open(file_name,'ab')
        np.save(f, out)
        f.close()

if 1:
    f = open(file_name, 'rb')
    f_size = os.fstat(f.fileno()).st_size
    print(f_size)
    lines = []
    time_sequence = []
    while f.tell() < f_size:
#         print(f.tell())
        line = np.load(f, allow_pickle=True)
#         print((line))
        lines.append(line)
    print(np.shape(lines))
    print(np.shape(lines[0]))
    print(np.shape(lines[0][0]))
#     print(np.shape(lines))

    
#     x_axis = np.linspace(0, len(time_sequence)-1, len(time_sequence))
# #     time_sequence = time_sequence[500:3500]
# #     x_axis = x_axis[500:3500]
#     fit_params = curve_fit(fit_func_line, np.linspace(0, len(time_sequence)-1, len(time_sequence)), time_sequence)
#     [p, q] = fit_params[0]
#     print(p)
#     linear_fit = np.linspace(0, len(time_sequence)-1, len(time_sequence)) * p + q
#     [p, q] = np.polyfit(x_axis, time_sequence, 1)
#     linear_fit = x_axis * p + q
    
#     plt.figure(1)
#     plt.subplot(2,1,1)
#     plt.plot(time_sequence, 'b', marker=' ')
#     plt.plot(linear_fit, 'r', marker=' ')
#     plt.grid(which='both', axis='both')
#     plt.subplot(2,1,2)
#     plt.plot(time_sequence-linear_fit)
#     plt.grid(which='both', axis='both')
#     plt.show()

# SmarAct_name_1 = r'C:\Users\yu03\Desktop\NMC Room\6 Dof PI\Rigid\np_16line\3_Noise_16line_10h_2.5Hz\1_SmarAct_CH1.bindata'
# SmarAct_name_2 = r'C:\Users\yu03\Desktop\NMC Room\6 Dof PI\Rigid\np_16line\3_Noise_16line_10h_2.5Hz\1_SmarAct_CH2.bindata'
# 
# if 1:
#     SmarAct_CH1 = np.fromfile(SmarAct_name_1, dtype='>d')
#     print('CH1: ', SmarAct_CH1.shape)
#     SmarAct_CH2 = np.fromfile(SmarAct_name_2, dtype='>d')
#     print('CH2: ', SmarAct_CH2.shape)
#     SmarAct_CH1 = SmarAct_CH1[(SmarAct_CH1<-1e-200) | (SmarAct_CH1>1e-200)]
#     print('CH1: ',SmarAct_CH1.shape)
#     SmarAct_CH2 = SmarAct_CH2[(SmarAct_CH2<-1e-200) | (SmarAct_CH2>1e-200)]
#     print('CH2: ',SmarAct_CH2.shape)
# 
#     plt.figure(1)
#     plt.plot(SmarAct_CH1)
#     plt.show()