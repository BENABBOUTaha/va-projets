# -*- coding: utf-8 -*-
"""
Created on Fri May 10 00:46:59 2019

@author: maazouz
"""

# =============================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ running averege $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# =============================================================================
import cv2
import numpy as np

video_from_hdd = cv2.VideoCapture('1.mp4')

_,avg = video_from_hdd.read()
avg = cv2.GaussianBlur(avg,(5,5),0)
avg = cv2.cvtColor(avg, cv2.COLOR_BGR2GRAY)
avg = np.float32(avg)

 
for _ in range(0,50):
    _,background = video_from_hdd.read()
    background = cv2.cvtColor(background, cv2.COLOR_RGB2GRAY)
    background = cv2.GaussianBlur(background,(5,5),0)
    cv2.accumulateWeighted(background,avg,0.01)
    res = cv2.convertScaleAbs(avg)



ok_flag = True
while ok_flag:
    _,img = video_from_hdd.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img,(5,5),0)
    new_img = cv2.absdiff(img,res)
    _,new_img = cv2.threshold(new_img,20,255,cv2.THRESH_BINARY)
    cv2.imshow(" frame differencig ", new_img)
    background = img
    # tab 'ESC'
    if cv2.waitKey(30) == 27:
        ok_flag = False

video_from_hdd.release()
cv2.destroyAllWindows()