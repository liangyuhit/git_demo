# -*- coding: utf-8 -*-
'''
Created on Mar 17, 2020

@author: yl
'''
from tqdm import tqdm
import time

for i in tqdm(range(100),ncols=80):
    time.sleep(0.1)
    j = i*i