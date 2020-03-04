"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

import os
import cv2
import json
import random
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from skimage import data, exposure, img_as_float


def display_augment_instance(image, aug_image, points, aug_points):
    img_vis = image.copy()
    for lane in points:
        cv2.polylines(img_vis, np.int32 ([lane]), isClosed=False, color=(0, 255, 255), thickness=4)
    aug_image_vis = aug_image.copy()
    for lane in aug_points:
        cv2.polylines(aug_image_vis, np.int32 ([lane]), isClosed=False, color=(0, 255, 255), thickness=4)
    plt.figure(figsize=(12,8))
    ax = plt.subplot(121)
    ax.imshow(img_vis[:, :, ::-1])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("origin image")

    ax = plt.subplot(122)
    ax.imshow (aug_image_vis[:, :, ::-1])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("augmentation image")
    plt.show()


def filter_invalid_point(points, h, w):
    aug_points = []
    for lane in points:
        temp = []
        for point in lane:
            if point[0] in range(0, w) and point[1] in range(0, h):
                temp.append(point)
        aug_points.append(temp)
    return aug_points


def random_scale_crop_pad(image, points):
    scale = random.uniform(2, 2.9)
    h, w, _ = image.shape
    aug_image = image.copy()
    aug_image = cv2.resize(aug_image, (int(scale * w), int(scale * h)))
    aug_points = []
    if (scale < 1.0):
        new_h, new_w, _ = aug_image.shape
        pre_h_pad = int((h - new_h) / 2)
        pre_w_pad = int((w - new_w) / 2)
        pad_list = [[pre_h_pad, h - new_h - pre_h_pad], [pre_w_pad, w - new_w - pre_w_pad], [0, 0]]
        aug_image = np.pad(aug_image, pad_list, mode="constant")
        for lane in points:
            temp = []
            for point in lane:
                temp.append((int(point[0] * scale + pre_w_pad), int(point[1] * scale + pre_h_pad)))
            aug_points.append(temp)

    if (scale > 1.0):
        new_h, new_w, _ = aug_image.shape
        pre_h_crop = int((new_h - h) / 2)
        pre_w_crop = int((new_w - w) / 2)
        post_h_crop = h + pre_h_crop
        post_w_crop = w + pre_w_crop
        aug_image = aug_image[pre_h_crop:post_h_crop, pre_w_crop:post_w_crop]
        for lane in points:
            temp = []
            for point in lane:
                temp.append((int(point[0] * scale - pre_w_crop), int(point[1] * scale - pre_h_crop)))
            aug_points.append(temp)
    aug_points = filter_invalid_point(aug_points, h, w)
    return aug_image, aug_points


if __name__=="__main__":
    root_dir = "/Users/alanwang/Downloads/train_set"
    file_list = os.listdir(root_dir)
    file_list = [item for item in file_list if item.endswith(".json")]
    dataset = []
    for name in file_list:
        path = os.path.join(root_dir, name)
        with open(path, encoding='utf-8') as f:
            for item in f.readlines():
                dataset.append(json.loads(item))
    id_index = random.choice(dataset)
    image = cv2.imread(os.path.join(root_dir, id_index["raw_file"]))
    lanes_points = [[(x, y) for (x, y) in zip(lane, id_index['h_samples']) if x >= 0] for lane in id_index["lanes"]]
    aug_image, aug_point = random_scale_crop_pad(image, lanes_points)
    display_augment_instance(image, aug_image, lanes_points, aug_point)