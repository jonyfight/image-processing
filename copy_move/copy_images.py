"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

import os
import shutil

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile) #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath) #创建路径
        shutil.copyfile(srcfile,dstfile) #复制文件
        print ("copy %s -> %s"%( srcfile,dstfile))