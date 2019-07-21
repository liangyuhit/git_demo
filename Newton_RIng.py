# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2019

@author: yl
'''
import numpy as np
import matplotlib.pyplot as plt

I_r_set = []
Lamda = 633e-9
Distance=np.linspace(0, Lamda/8,4)
for D in Distance:
    R = 5
    r = np.linspace(start=0, stop=0.005, num=1001)
    d = R - np.sqrt(R**2 - r**2)
    A = 2 * np.pi * (d+2*D) / Lamda
    I_r = np.sin(A)**2
    I_r_set.append(I_r)

plt.figure(1)
for i in range(len(Distance)):
    plt.plot(r, I_r_set[i])
plt.show()

Lamda = 633e-9
# R = 1
pix_size = 5.3e-6
pix_num = 1001
D=np.pi/2
center = [(pix_num-1)*pix_size/2, (pix_num-1)*pix_size/2]
dx = np.linspace(0, (pix_num-1)*pix_size, num=pix_num)
dy = dx
dx, dy = np.meshgrid(dx, dy)
r = np.sqrt((dx-center[0])**2 + (dy-center[1])**2)
d = R - np.sqrt(R**2 - r**2)
A = 2 * np.pi * (d+2*D) / Lamda
I_r = np.sin(A)**2
tau0 = pix_size
fs = 1/tau0
N = len(dx)

plt.figure('Simulated Pattern')
# plt.subplot(1,2,1)
plt.title("Whole Frame")
plt.imshow(I_r, cmap='gray')
plt.show()