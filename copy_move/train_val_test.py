# -*- coding:utf-8 -*-

"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

#!/usr/bin/env python

# 将一个文件夹下图片按比例分在两个文件夹下，比例改0.7这个值即可
import os
import random
import shutil
from shutil import copy2

trainfiles = os.listdir('D:\\train\\img\\image')  #（图片文件夹）
num_train = len(trainfiles)
print( "num_train: " + str(num_train) )
index_list = list(range(num_train))
print(index_list)
random.shuffle(index_list)
num = 0
trainDir = 'D:\\train\\img\\image_train'  #（将图片文件夹中的7份放在这个文件夹下）
validDir = 'D:\\train\\img\\image_valid'  #（将图片文件夹中的3份放在这个文件夹下）
for i in index_list:
    fileName = os.path.join('D:\\train\\img\\image', trainfiles[i])
    if num < num_train*0.7:
        print(str(fileName))
        copy2(fileName, trainDir)
    else:
        copy2(fileName, validDir)
    num += 1