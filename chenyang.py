'''
Created on 12.11.2019

@author: yu03
'''

import numpy as np

def f_cy(a,b,c):
    return a+b+c

A = [1, 2, 3]
B = [4, 5, 6]
C = [10, 20, 30]

for i in range(3):
    print(f_cy(A[i], B[i], C[i]))