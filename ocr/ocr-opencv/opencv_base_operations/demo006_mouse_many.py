# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 11:22
# @Author  : JackNiu
# @File    : demo006_mouse_many.py
# @Software: PyCharm

import cv2
import numpy as np

drawing = False
mode = False
ix,iy =-1,-1

def draw_cicle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True
        print(x,y)
        ix,iy= x,y
    if event  == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode ==True:
            print(x,y)
            cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_cicle)

while(True):
    cv2.imshow('image', img)
    k = cv2.waitKey(0) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()
