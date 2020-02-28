# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 10:14
# @Author  : JackNiu
# @File    : demo001_base.py
# @Software: PyCharm

import cv2
import numpy as np

# 加载图片，灰度模式
img = cv2.imread('D:\Project\WeixinGGG\ocr\ocr-opencv\opencv_base_operations\img\\47decf3cd5f98075d951a13f8868e4c.jpg',0)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('D:\Project\WeixinGGG\ocr\ocr-opencv\opencv_base_operations\img\\youna.png',img)
    cv2.destroyAllWindows()