# -*- coding: utf-8 -*-
'''
Created on Jan 9, 2021

@author: yl
'''

import numpy as np
# import matplotlib.pyplot as plt

num = 1000
array = np.linspace(0,num-1,num)
# print(array)
results = []
for start_point in range(len(array)-1):
#     print(start_point)
    for index in range(len(array)-start_point-1):
        stop_point = index + start_point + 1
#         print(stop_point)
        mid = (start_point + stop_point) / 2
        results.append(mid)
results = sorted(results)
# print(results)
final = list()
for i in results:
    if i not in final:
        final.append(i)
# print(final)
print(len(final))
        