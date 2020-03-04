"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

#将特定文件夹下的文件移动到另一个文件夹
import os
import shutil

path_xml = "D://5"#windows系统用双斜线
filelist = os.listdir(path_xml)
path1 = "D:\\5"
path2 = "D:\\5\\jpg\\"


for files in filelist:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  #读取文件名
    print(filename1)
    m = filename1 == '.png'
    print(m)
    if m :
        full_path = os.path.join(path1, files)
        despath = path2 + filename0+'.png' #.jpg为你的文件类型，即后缀名，读者自行修改
        shutil.move(full_path, despath)

    else :
        continue