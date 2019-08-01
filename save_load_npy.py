# -*- coding: utf-8 -*-
'''
Created on 31.07.2019

@author: yu03
'''
import numpy as np
import os

file_name = r'C:\Users\yu03\eclipse-workspace\git_demo\test.npy'

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
    while f.tell() < f_size:
        print(f.tell())
        line = np.load(f, allow_pickle=True)
        print(line)
        lines.append(line)
    print(len(lines))