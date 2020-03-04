"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

# -*- coding:utf8 -*-

import os

class BatchRename():
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self):
        # self.path = 'E:/Smart Image Project/Images Classification/pytorch_hand_classifier-master/data/images/train/3'
        # self.path = "E:/Smart_Image_Project/Images_Classification/pytorch_hand_classifier-master/data/images/train1/1"
        self.path = "F:/data_images2/test_origin/1"

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 43
        for item in filelist:
            if item.endswith('.png'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.png')
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d pngs' % (total_num, i))

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()