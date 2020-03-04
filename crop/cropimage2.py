"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

from PIL import Image
#裁剪压缩图片

def clipResizeImg(**args):
  args_key = {'ori_img':'','dst_img':'','dst_w':'','dst_h':'','save_q':75}
  arg = {}
  for key in args_key:
    if key in args:
      arg[key] = args[key]
  im = Image.open(arg['ori_img'])
  ori_w,ori_h = im.size
  dst_scale = float(arg['dst_h']) / arg['dst_w'] #目标高宽比
  ori_scale = float(ori_h) / ori_w #原高宽比
  if ori_scale >= dst_scale:
    #过高
    width = ori_w
    height = int(width*dst_scale)
    x = 0
    y = (ori_h - height) / 3
  else:
    #过宽
    height = ori_h
    width = int(height*dst_scale)
    x = (ori_w - width) / 2
    y = 0
  #裁剪
  box = (x,y,width+x,height+y)
  #这里的参数可以这么认为：从某图的(x,y)坐标开始截，截到(width+x,height+y)坐标
  #所包围的图像，crop方法与php中的imagecopy方法大为不一样
  newIm = im.crop(box)
  im = None
  #压缩
  ratio = float(arg['dst_w']) / width
  newWidth = int(width * ratio)
  newHeight = int(height * ratio)
  newIm.resize((newWidth,newHeight),Image.ANTIALIAS).save(arg['dst_img'],quality=arg['save_q'])