# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:34:57 2019
@author: maazouz
"""
# =============================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ frame differencig $$$$$$$$$$$$$$$$$$$$$$$$$$$
# =============================================================================
import cv2

video_from_hdd = cv2.VideoCapture('1.mp4')

_,background = video_from_hdd.read()
background = cv2.cvtColor(background, cv2.COLOR_RGB2GRAY)
background = cv2.GaussianBlur(background,(5,5),0)

ok_flag = True
while ok_flag:
    _,img = video_from_hdd.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img,(5,5),0)
    new_img = cv2.absdiff(img,background)
    _,new_img = cv2.threshold(new_img,20,255,cv2.THRESH_BINARY)
    cv2.imshow(" frame differencig ", new_img)
    background = img
    # tab 'ESC'
    if cv2.waitKey(30) == 27:
        ok_flag = False

video_from_hdd.release()
cv2.destroyAllWindows()