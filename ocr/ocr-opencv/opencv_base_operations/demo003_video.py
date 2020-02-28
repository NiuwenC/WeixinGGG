# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 10:56
# @Author  : JackNiu
# @File    : demo003_video.py
# @Software: PyCharm

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('vtest.avi')
while(True):
    #一帧一帧的读取
    ret,frame= cap.read()

    # frame = np.array(frame,dtype=np.uint8)
    #
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()