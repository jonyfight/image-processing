"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

import os
import shutil
import multiprocessing


#读取文件路径
def read_data_path(data_path,hidename):
    """
    内部功能函数：对文件夹路径下文件的进行搜索，并对其文件格式进行筛选
    :param data_path: 文件夹路径
    :param hidename: 文件筛选格式
    :return: 返回2个列表[filename][filepath]
    """
    #遍历文件夹内所有文件
    outputpath = []
    outputname = []
    for dirpath, dirnames, filenames in os.walk(data_path):
        for filename in filenames:
            #进行扩展名筛选
            if os.path.splitext(filename)[1] == ('.' + hidename) :
                path = [dirpath ,filename]
                outputpath.append(dirpath)
                outputname.append(filename)
    return outputpath,outputname

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile) #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath) #创建路径
        shutil.move(srcfile,dstfile) #移动文件
        print ("move %s -> %s"%( srcfile,dstfile))


def random_move(fn):
    path1 = r"F:\data_images2\test\0"
    path2 = r"F:\data_images2\test\others"
    # i, j = read_data_path(path, "png")
    i = fn[0]
    j = fn[1]
    sign = fn[0].split(os.path.sep)[-1]
    if sign == '0':
        o_path = os.path.join(i, j) * 0.2
        mymovefile(o_path, os.path.join(path1, j))
    else:
        others_path = os.path.join(i, j) * 0.3
        if not os.path.exists(os.path.join(path2, sign)):
            os.mkdir(os.path.join(path2, sign))
        mymovefile(others_path, os.path.join(path2, sign, j))
    # return a


def main(filepath):
    # path1 = r"F:\data_images\0"
    # path2 = r"F:\data_images\others"
    a, b = read_data_path(filepath, "png")
    testFL = []
    for i, j in zip(a, b):
        testFL.append([i,j])
        # if i == "0" and j in "0":
        #     mycopyfile(os.path.join(i, j), os.path.join(path1, j))
        # else:
        #     mycopyfile(os.path.join(i, j), os.path.join(path2, j))
    pool = multiprocessing.Pool(processes=6)
    a = pool.map(random_move, testFL)
    pool.close()
    pool.join()
    print(len(a))

if __name__=="__main__":
    path = r"F:\data_images2\test"
    read_data_path(path,"png")