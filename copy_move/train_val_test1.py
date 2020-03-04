# -*- coding:utf-8 -*-

"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

# !/usr/bin/env python
# 将一个文件夹下图片按比例分在三个文件夹下
import os
import random
import shutil
from shutil import copy2

datadir_normal = "./fundus_data_pres/Normal/images/"

all_data = os.listdir(datadir_normal)  # （图片文件夹）
num_all_data = len(all_data)
print("num_all_data: " + str(num_all_data))
index_list = list(range(num_all_data))
# print(index_list)
random.shuffle(index_list)
num = 0

trainDir = "./fundus_data/train/normal/"  # （将训练集放在这个文件夹下）
if not os.path.exists(trainDir):
    os.mkdir(trainDir)

validDir = './fundus_data/val/normal/'  # （将验证集放在这个文件夹下）
if not os.path.exists(validDir):
    os.mkdir(validDir)

testDir = './fundus_data/test/normal/'  # （将测试集放在这个文件夹下）
if not os.path.exists(testDir):
    os.mkdir(testDir)

for i in index_list:
    fileName = os.path.join(datadir_normal, all_data[i])
    if num < num_all_data * 0.6:
        # print(str(fileName))
        copy2(fileName, trainDir)
    elif num > num_all_data * 0.6 and num < num_all_data * 0.8:
        # print(str(fileName))
        copy2(fileName, validDir)
    else:
        copy2(fileName, testDir)
    num += 1
