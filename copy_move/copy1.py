"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

import os
import shutil

def imageslocation(filepath):
    name = os.listdir(filepath)
    name1 = os.listdir(filepath + "\\0")
    return name1

def copyimages(filepath):
    path1 = r"F:\data_images\0"
    path2 = r"F:\data_images\others"
    name = os.listdir(filepath)
    for i in name:
        if i == "0":
            mycopyfile(os.listdir(filepath + "/0"),path1 + os.listdir(filepath + "/0"))
        else:
            others_path = os.path.join(filepath,i)
            # others_path = str(others_path)
            mycopyfile(os.listdir(others_path),path2)
    # print(os.listdir())

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile) #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath) #创建路径
        shutil.move(srcfile,dstfile) #移动文件
        print ("move %s -> %s"%( srcfile,dstfile))


def mycopyfile(srcfile, dstfile):
    # fpath, fname = os.path.split(dstfile)
    # if not os.path.exists(fpath):
    shutil.copy(srcfile, dstfile)
    print("copy %s -> %s"%( srcfile,dstfile))

# def mycopyfile(srcfile,dstfile):
#     if not os.path.isfile(srcfile):
#         print ("%s not exist!"%(srcfile))
#     else:
#         fpath,fname=os.path.split(dstfile) #分离文件名和路径
#         if not os.path.exists(fpath):
#             os.makedirs(fpath) #创建路径
#         shutil.copyfile(srcfile,dstfile) #复制文件
#         print ("copy %s -> %s"%( srcfile,dstfile))


if __name__=="__main__":
    path = r"E:\Smart_Image_Project\Images_Classification\image"
    # print(imageslocation(path))
    copyimages(path)