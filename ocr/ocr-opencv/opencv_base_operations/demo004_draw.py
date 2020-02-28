# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 11:08
# @Author  : JackNiu
# @File    : demo004_draw.py
# @Software: PyCharm

'''
目标是学习如何画不同的图形
cv2.line
cv2.cicle
cv2.rectangle
'''
import numpy as np
import cv2

# img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('D:\Project\WeixinGGG\ocr\ocr-opencv\opencv_base_operations\img\\47decf3cd5f98075d951a13f8868e4c.jpg')

# img = cv2.line(img,(0,0),(511,511),(125,124,0),5)
# img = cv2.rectangle(img,(10,18),(125,125),(0,255,0),3)
# img = cv2.circle(img,(477,63),13,(0,200,123),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'JackNiu',(100,500),font,4,(255,255,255),3,cv2.LINE_AA)

cv2.imshow('line',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()