# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:43:00 2019

@author: maazouz
"""

# =============================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ mean_filter.py $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# =============================================================================

import cv2
import numpy as np

ok_flag = True
video_from_hdd = cv2.VideoCapture('1.mp4')
list_of_images = []

for _ in range(0,3):
    _,background = video_from_hdd.read()
    background = cv2.cvtColor(background, cv2.COLOR_RGB2GRAY)
    background = cv2.GaussianBlur(background,(5,5),0)
    list_of_images.append(background)

while ok_flag:
    _,img = video_from_hdd.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img,(5,5),0)
    # build a matrix of 10 images
    matrix = np.array(list_of_images)
    #calculate avg of each cell in matrix (mean apply to np.array type)
    #mean return float as result then u must converted to uint8 using astype
    finally_background = matrix.mean(0).astype('uint8')

    new_img = cv2.absdiff(img,finally_background)
    _,new_img = cv2.threshold(new_img,20,255,cv2.THRESH_BINARY)
    cv2.imshow(" mean filter ", new_img)
    #remove the first image from list and displace images to front
    list_of_images.pop(0)
    # add new image in last position of list
    list_of_images.append(img)
    
    # tab 'ESC'
    if cv2.waitKey(30) == 27:
        ok_flag = False

video_from_hdd.release()
cv2.destroyAllWindows()