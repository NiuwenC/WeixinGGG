# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 10:47
# @Author  : JackNiu
# @File    : demo002_matplotlib.py
# @Software: PyCharm

import numpy as np
import cv2
from  matplotlib  import pyplot as plt

img = cv2.imread('D:\Project\WeixinGGG\ocr\ocr-opencv\opencv_base_operations\img\\47decf3cd5f98075d951a13f8868e4c.jpg',0)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])  #隐藏tick值
plt.show()
