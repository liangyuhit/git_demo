# -*- coding: utf-8 -*-
'''
Created on 23.05.2020

@author: yu03
'''
import glob
import os
import shutil

'''
    定义文件夹路径，以桌面上的文件夹为例
'''
path = r'C:\Users\yu03\Desktop\test'

for file in glob.glob(path+r'\*.pdf'): #对路径下的每个.pdf文件进行操作
    print(file)
#     print(file.split('\\'))
#     print(file.split('\\')[-1])
#     print(file.split('\\')[-1].split('.')[0])
    '''
            提取出文件名
    '''
    file_name = file.split('\\')[-1].split('.')[0]
    '''
            创建一个相应的新文件夹
    '''
    os.mkdir(path+'\\'+file_name)
    '''
            定义目标路径
    '''
    path_new = path + '\\' + file_name + '\\' + file_name + '.pdf'
    shutil.copy(file, path_new)
    
    
    