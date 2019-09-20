# -*- coding: utf-8 -*-
'''
Created on 19.09.2019

@author: yu03
'''
import numpy as np

def Read_Data_3Ch(name):
    '''
        Return Data in File (4 Channels: Data_Ch1, Data_Ch2)
        File name required (default path)
    '''
    print('Reading Data PI')
    with open(name,'r') as fid:
        line=''
        while line[0:4] != '----':
            line = fid.readline()
#             print(line)
            if line[0:2] == 'Fs':
                p, q, m, n = line.strip().split(' ')
                fs_cam = float(m)
                print('fs_cam = %f\n'%fs_cam)
        out_str = fid.readlines()
    Data_Ch1, Data_Ch2, Data_Ch3 = [], [], []
    for line in out_str:
        a, b, c= line.strip().split(', ')
        Data_Ch1.append(float(a))
        Data_Ch2.append(float(b))
        Data_Ch3.append(float(c))
    Data_Ch1 = np.array(Data_Ch1)
    Data_Ch2 = np.array(Data_Ch2)
    Data_Ch3 = np.array(Data_Ch3)
    return Data_Ch1, Data_Ch2, Data_Ch3

path = r'C:\Users\yu03\Desktop\NMC Room\6 Dof PI\Rigid\Cam\Nonlinearity_hor\2__1urad_50s'
name = '2'
type = '.txt'

PI_name = path + '\\' +  name + '_PI' + type

'''
    Reading PI 6Dof
'''
length_PI, Hor_PI, Ver_PI = Read_Data_3Ch(PI_name)
print('PI: ', len(length_PI))