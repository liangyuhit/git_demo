# -*- coding: utf-8 -*-
'''
Created on Aug 4, 2019

@author: yl
'''
import numpy as np
import matplotlib.pyplot as plt

j = complex(0, 1)
c = 3e8 # 光速 [m/s]
Lamda = 633e-9 # 光波长 [m]
Fc = c / Lamda # 光频率 [Hz]
k = 2 * np.pi / Lamda

P_1= 1e-3 #功率
w0_1 = 1800e-6
Z_R_1 = np.pi * w0_1**2 / Lamda
print(Z_R_1)
P_2= 1e-3 #功率
w0_2 = 1800e-6
Z_R_2 = np.pi * w0_2**2 / Lamda

Z_pos_1 = 0.1
# Z_pos_1 = np.linspace(-10, 10, 1000)
w_z_1 = w0_1 * np.sqrt(1 + Z_pos_1**2/Z_R_1**2)
R_z_1 = Z_pos_1 * (1 + Z_R_1**2/Z_pos_1**2)
# print(R_z)
Gouy_Z_1 = np.arctan(Z_pos_1/Z_R_1)
[center_1_x, center_1_y] = [0, 0]
# plt.figure(1)
# plt.plot(Z_pos_1, R_z_1)
# plt.show()

Z_pos_2 = 0.1
w_z_2 = w0_2 * np.sqrt(1 + Z_pos_2**2/Z_R_2**2)
R_z_2 = Z_pos_2 * (1 + Z_R_2**2/Z_pos_2**2)
# print(R_z)
Gouy_Z_2 = np.arctan(Z_pos_2/Z_R_2)
[center_2_x, center_2_y] = [0.002, 0.002]
 
 
X = np.linspace(-0.005, 0.005, num=301)
Y = X
x, y = np.meshgrid(X, Y)
r_1 = np.sqrt((center_1_x-x)**2 + (center_1_y-y)**2)
A_1 = np.sqrt(2*P_1/np.pi/(w_z_1**2)) * np.exp(-r_1**2/w_z_1**2)
Phi_1 = k*r_1**2/2/R_z_1 - Gouy_Z_1 + k*Z_pos_1
r_2 = np.sqrt((center_2_x-x)**2 + (center_2_y-y)**2)
A_2 = np.sqrt(2*P_2/np.pi/(w_z_2**2)) * np.exp(-r_2**2/w_z_2**2)
Phi_2 = k*r_2**2/2/R_z_2 - Gouy_Z_2 + k*Z_pos_2
A = (A_1+A_2)**2
# E = A * np.exp(j * (2*np.pi*Fc*t-Phi))
plt.figure(1)
c = plt.gca().pcolor(X, Y, A, cmap='gray')
plt.xlabel('dx [mm]')
plt.ylabel('dy [mm]')
plt.colorbar(c, ax=plt.gca())
 
plt.show()
