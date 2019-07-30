# -*- coding: utf-8 -*-
'''
Created on Jul 30, 2019

@author: yl
'''
import numpy as np
# import datetime

file_name = 'test.txt'

# f = open(file_name,'a')
# for i in range(10):
#     a = np.random.randint(0,255,size=10)
#     np.savetxt(f, a, fmt='%i', delimiter=',', newline=' ')
#     f.write('\n')
#     print(a)

f = open(file_name,'r')
lines = f.readlines()
# print(lines)
for line in lines:
    x = np.empty([1,10], dtype = int) 
    print(x)
    x = line.strip().split(' ')
    print(x)
    
        
        
        