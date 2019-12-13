# -*- coding: utf-8 -*-
'''
Created on Jul 30, 2019

@author: yl
'''
import numpy as np
import datetime
from skimage.feature.tests.test_util import plt

now = datetime.datetime.now()

file_name = r'F:\Data_Liang_Yu\Users\yu03\Desktop\3-DoF Interferometer\NMC Room\6 Dof PI\Rigid\np_16line\Noise & Stability closedmode\6_Noise_16line_10bit_1Hz\PTB record\Data_cut.txt'
header = ['%s\n' %file_name,
        'Local current time : %s\n' %now.strftime("%Y-%m-%d %H:%M:%S"),
        '-------------------------------------------------\n',
        ]

if 0:
    #### Header Writing
    f = open(file_name,'w')
    f.writelines(header)
    #### Data writing
    
    for i in range(10):
        f = open(file_name,'a')
        a = np.random.randint(0,255,size=10)
        np.savetxt(f, a, fmt='%i', delimiter=',', newline=' ')
        f.write('\n')
        f.close()
        print(a)

if 0:
    f = open(file_name,'r')
    line_header=''
    while line_header[0:4] != '----':
        line_header = f.readline()
        print(line_header.strip())
    
    lines = f.readlines()
    print(lines)
    for line in lines:
        x = line.strip().split(' ')
        x = [int(k) for k in x]
        print(x)

if 1:
    time_set = []
    pressure_set = []
    humidity_set = []
    n_633_set = []
    
    f = open(file_name,'r')
    lines = f.readlines()
#     print(lines)
    for line in lines:
        x = line.strip().split(' ')
        x = [float(k) for k in x]
        print(x)
        [time, pressure, humidity, n_633, n1532] = x
        time_set.append(time)
        pressure_set.append(pressure)
        humidity_set.append(humidity)
        n_633_set.append(n_633)
    time_set = np.array(time_set)
    pressure_set = np.array(pressure_set)
    humidity_set = np.array(humidity_set)
    n_633_set = np.array(n_633_set)

    plt.figure(1)
#     plt.subplot(3,1,1)
    plt.plot(time_set, -pressure_set,label='pressure')
    plt.grid(which='both',axis='both')
#     plt.subplot(3,1,2)
#     plt.plot(time_set, humidity_set,label='humidity')
#     plt.grid(which='both',axis='both')
#     plt.subplot(3,1,3)
#     plt.plot(time_set, n_633_set,label='air index 633')
#     plt.grid(which='both',axis='both')
    plt.legend()
    plt.show()
        
        