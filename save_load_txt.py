# -*- coding: utf-8 -*-
'''
Created on Jul 30, 2019

@author: yl
'''
import numpy as np
import datetime

now = datetime.datetime.now()

file_name = 'test.txt'
header = ['%s\n' %file_name,
        'Local current time : %s\n' %now.strftime("%Y-%m-%d %H:%M:%S"),
        '-------------------------------------------------\n',
        ]

if 0:
    #### Header Writing
    f = open(file_name,'w')
    f.writelines(header)
    #### Data writing
    f = open(file_name,'a')
    for i in range(10):
        a = np.random.randint(0,255,size=10)
        np.savetxt(f, a, fmt='%i', delimiter=',', newline=' ')
        f.write('\n')
        print(a)

if 1:
    f = open(file_name,'r')
    line_header=''
    while line_header[0:4] != '----':
        line_header = f.readline()
        print(line_header.strip())
    
    lines = f.readlines()
    for line in lines:
        x = line.strip().split(' ')
        x = [int(k) for k in x]
        print(x)
        
        
        