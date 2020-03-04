#coding: utf-8

"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""


"""
采用多进程加快处理。添加了在读取图片时捕获异常，OpenCV对大分辨率或者tif格式图片支持不好
处理数据集 和 标签数据集的代码：（主要是对原始数据集裁剪）
    处理方式：分别处理
    注意修改 输入 输出目录 和 生成的文件名
    output_dir = "./label_temp"
    input_dir = "./label"
"""

import multiprocessing
import cv2
import os
import time
import numpy as np


def get_img(input_dir):
    img_paths = []
    for (path,dirname,filenames) in os.walk(input_dir):
        for filename in filenames:
            img_paths.append(path+'/'+filename)
    print("img_paths:",img_paths)
    return img_paths


def cut_img(img_paths,output_dir):
    imread_failed = []
    try:
        # for i in range(np.randint(4)):
        y = np.random.randint(0, 932)  # 原图大小为1906*1348，如果是要生成416*416大小图片，需要修改参数（932,1490）.512为（836,1394）
        x = np.random.randint(0, 1490)
        img = cv2.imdecode(np.fromfile(img_paths, dtype=np.uint8), -1)
        # img = cv2.imread(img_paths)
        # height, weight = img.shape[:2]
        # if (1.0 * height / weight) < 1.3:       # 正常发票
        cropImg = img[y:y + 416, x:x + 416]     # 裁剪【y1,y2：x1,x2】,img[50:200, 700:1500]/img[y:y + 416, x:x + 416]
        cv2.imencode('.png', cropImg)[1].tofile(output_dir + '/' + img_paths.split('/')[-1])
        # cv2.imwrite(output_dir + '/' + img_paths.split('/')[-1], cropImg)
        # else:                                   # 卷帘发票
        #     cropImg_01 = img[30:150, 50:600]
        #     cv2.imwrite(output_dir + '/' + img_paths.split('/')[-1], cropImg_01)
    except:
        imread_failed.append(img_paths)
    return imread_failed


def main(input_dir,output_dir):
    img_paths = get_img(input_dir)
    scale = len(img_paths)

    results = []
    pool = multiprocessing.Pool(processes = 4)
    for i,img_path in enumerate(img_paths):
        a = "#"* int(i/10)
        b = "."*(int(scale/10)-int(i/10))
        c = (i/scale)*100
        results.append(pool.apply_async(cut_img, (img_path,output_dir )))
        print('{:^3.3f}%[{}>>{}]'.format(c, a, b)) # 进度条（可用tqdm）
    pool.close()                        # 调用join之前，先调用close函数，否则会出错。
    pool.join()                         # join函数等待所有子进程结束
    count = 0
    for result in results:
        count += 1
        print('image read failed!:', result.get())
    print(count)
    print ("All done.")



if __name__ == "__main__":
    # input_dir = "D:/image_person"       # 读取图片目录表
    # output_dir = "D:/image_person_02"   # 保存截取的图像目录
    input_dir = "F:/data_images2/test1/1"  # 路径0为负样本
    output_dir = "F:/data_images2/test/1"  # 512*512为路径1,416*416为2
    main(input_dir, output_dir)