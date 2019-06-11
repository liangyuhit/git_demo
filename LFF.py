# -*- coding: utf-8 -*-
'''
Created on Jun 9, 2019

@author: yl
'''

rice_unit = 1 ### kJ/g
jogurt_unit = 3.81 ### kJ/g

rice_amount = 100
jogurt_amount = 50
 
heat = rice_unit * rice_amount + jogurt_unit * jogurt_amount

print(heat)