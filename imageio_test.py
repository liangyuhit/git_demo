# -*- coding: utf-8 -*-
'''
Created on 06.07.2020

@author: yu03
'''
import imageio
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import glob
import os
import shutil
from matplotlib.gridspec import GridSpec
import matplotlib.patches as patches

j = complex(0, 1)
c = 3e8 # 光速 [m/s]
Lamda = 633e-9 # 光波长 [m]
Fc = c / Lamda # 光频率 [Hz]

pix_size = 5.3e-6
pix_num = 200
screen_diameter = pix_num * pix_size


dx = np.linspace(0, (pix_num-1)*pix_size, num=pix_num)
dy = dx
V_r_x, V_r_y, V_r_z = 0.00, 0.00, 1 # Reference vector
L, D = 0.1, 0.1  # D = displacement, L is static
V_m_x, V_m_y, V_z_m = 0, 0.000, 1 # Measurement vector

X, Y = np.meshgrid(dx, dy)

def f(X, Y):
    '''
        Window 2d
    '''
    window = signal.gaussian(pix_num, std=pix_num/8)
    window_x, window_y = np.meshgrid(window, window)
    window_2d = window_x*window_y
    
    k = 2 * np.pi / Lamda
    I_0 = 512
    
    '''
        Wave Generating
    '''
    diff_Z_p = D * 2 / (1-V_m_x**2-V_m_y**2) + L * 2 * ((V_m_x**2+V_m_y**2)-(V_r_x**2+V_r_y**2)) / (1-V_m_x**2-V_m_y**2) / (1-V_r_x**2-V_r_y**2)
#     d_ref = X*2*V_r_x*(1-V_r_x**2-V_r_y**2)/(1-V_r_x**2)/(1+V_r_x**2+V_r_y**2) + Y*2*V_r_y*(1-V_r_x**2-V_r_y**2)/(1-V_r_y**2)/(1+V_r_x**2+V_r_y**2) - L*4*(V_r_x**2+V_r_y**2)/(1-(V_r_x**2+V_r_y**2)**2)
#     d_mea = X*2*V_m_x*(1-V_m_x**2-V_m_y**2)/(1-V_m_x**2)/(1+V_m_x**2+V_m_y**2) + Y*2*V_m_y*(1-V_m_x**2-V_m_y**2)/(1-V_m_y**2)/(1+V_m_x**2+V_m_y**2) - (L+D)*4*(V_m_x**2+V_m_y**2)/(1-(V_m_x**2+V_m_y**2)**2)
    d_mea = (X*2*V_m_x+Y*2*V_m_y)/(1+V_m_x**2+V_m_y**2) - (L+D)*4*(V_m_x**2+V_m_y**2)/(1-(V_m_x**2+V_m_y**2)**2)
    d_ref = (X*2*V_r_x+Y*2*V_r_y)/(1+V_r_x**2+V_r_y**2) - L*4*(V_r_x**2+V_r_y**2)/(1-(V_r_x**2+V_r_y**2)**2)
    diff_phi = k * (diff_Z_p + (d_mea-d_ref))
    I_beat = I_0*(1+np.cos(diff_phi))
#     I_beat = I_beat.astype(np.int)
    
    '''
        Wave Generating (2nd way)
    '''
    D_d = D + X * (V_m_x - V_r_x) + Y * (V_m_y - V_r_y)
    L_d = L + X * V_r_x + Y * V_r_y
    diff_L_d_2 = D_d + (L_d + D_d) * (1 - (V_m_x**2 + V_m_y**2)) / (1 + (V_m_x**2 + V_m_y**2)) - L_d * (1 - (V_r_x**2 + V_r_y**2)) / (1 + (V_r_x**2 + V_r_y**2))
    Z = I_0 * (1 + np.cos(2 * np.pi * diff_L_d_2 / Lamda))
    
    return (I_beat) * window_2d

path = r'C:\Users\yu03\Desktop\imageio_test'
images = []
'''
    Generating image set
'''
fig = plt.figure()
fig.set_size_inches(10, 3, True)
gs = GridSpec(1, 2, width_ratios=[3, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

if 1:
    for i in range(10):
        D = D + Lamda/8
        img = ax2.imshow(f(X, Y),cmap='gray')
        img.set_clim([0,1000])
        plt.savefig(path+'\\'+'%s.jpg'%i)
'''
    Reading images
'''   
if 1:
    for file in glob.glob(path+r'\*.jpg'): #对路径下的每个.pdf文件进行操作
        img = imageio.imread(file)
        images.append(img)
    print(len(images))
    imageio.mimsave(r'C:\Users\yu03\Desktop\imageio_test.gif', images)
