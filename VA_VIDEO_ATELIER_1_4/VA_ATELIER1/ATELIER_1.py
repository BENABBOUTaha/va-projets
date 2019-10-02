# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:27:31 2019

@author: maazouz
"""

import cv2
cv2.__version__

video_from_cam = cv2.VideoCapture(0)
video_from_hdd = cv2.VideoCapture('1.mp4')

ok_flag = True
# Check if camera opened successfully
if (video_from_cam.isOpened()== False): 
  print("Error opening video stream or file")
  
while ok_flag:
    _,cam = video_from_cam.read()
    _,hdd = video_from_hdd.read()
    cv2.imshow("camera", cam)
    cv2.imshow("HDD", hdd)
    # tab 'ESC'
    if cv2.waitKey(30) == 27:
        ok_flag = False

video_from_cam.release()
video_from_hdd.release()
cv2.destroyAllWindows()