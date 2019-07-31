# -*- coding: utf-8 -*-
'''
Created on 31.07.2019

@author: yu03
'''
import numpy as np

file_name = r'C:\Users\yu03\eclipse-workspace\git_demo\test.npy'

if 0:
    for i in range(10):
        a = np.zeros(3)
        b = np.random.randint(0,5,3)
        c = 100
        out = np.array([a,b,c])
        print(out)
        f = open(file_name,'ab')
        np.save(f, out)

if 1:
    f = open(file_name, 'rb')
    a = np.load(f, allow_pickle=True)
    print(a)
    print(len(a))