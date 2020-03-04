# -*- coding: utf-8 -*-

"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

"""
处理数据集 和 标签数据集的代码：（主要是对原始数据集裁剪）
    处理方式：分别处理
    注意修改 输入 输出目录 和 生成的文件名
    output_dir = "./label_temp"
    input_dir = "./label"
"""
import cv2
import os
import sys
import time
import numpy as np

# img = cv2.imread('E:/Smart Image Project/Images Classification/pytorch_hand_classifier-master/data/images/1/佛肇区域-翡翠山-洋房-1#-原始-0.png')
# img = cv2.imread("E:/Smart Image Project/Images Classification/pytorch_hand_classifier-master/data/images/1")

def get_img(input_dir):
    img_paths = []
    for (path,dirname,filenames) in os.walk(input_dir):
        for filename in filenames:
            img_paths.append(path+'/'+filename)
    print("img_paths:",img_paths)
    return img_paths


def cut_img(img_paths,output_dir):
    scale = len(img_paths)
    for i,img_path in enumerate(img_paths):
        a = "#"* int(i/1000)
        b = "."*(int(scale/1000)-int(i/1000))
        c = (i/scale)*100
        time.sleep(0.2)
        print('正在处理图像： %s' % img_path.split('/')[-1])
        img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
        # img = cv2.imread(img_path)
        weight = img.shape[1]
        if weight>1600:                         # 正常发票
            cropImg = img[50:200, 700:1500]    # 裁剪【y1,y2：x1,x2】
            #cropImg = cv2.resize(cropImg, None, fx=0.5, fy=0.5,
                                 #interpolation=cv2.INTER_CUBIC) #缩小图像
            cv2.imwrite(output_dir + '/' + img_path.split('/')[-1], cropImg)
        else:                                        # 卷帘发票
            cropImg_01 = img[30:150, 50:600]
            cv2.imwrite(output_dir + '/'+img_path.split('/')[-1], cropImg_01)
        print('{:^3.3f}%[{}>>{}]'.format(c,a,b))

if __name__ == '__main__':
    output_dir = "E:/Smart Image Project/Images Classification/pytorch_hand_classifier-master/data/images/train/1"           # 保存截取的图像目录 ../img_cut
    input_dir = "E:/Smart Image Project/Images Classification/pytorch_hand_classifier-master/data/images/1"                # 读取图片目录表 ../img
    img_paths = get_img(input_dir)
    print('图片获取完成 。。。！')
    cut_img(img_paths,output_dir)
