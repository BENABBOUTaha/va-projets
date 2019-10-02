# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:35:36 2019

@author: EL KHOU Mohammed
"""

# Defference d'images _ Frame differencing
import cv2

cap = cv2.VideoCapture(0)

ret, current_frame = cap.read()
previous_frame = current_frame

while(cap.isOpened()):
    
#    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
#    previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)    
#    frame_diff = cv2.absdiff(current_frame_gray,previous_frame_gray)
#    frame_diff = abs(current_frame_gray-previous_frame_gray)
    
    frame_diff = cv2.absdiff(current_frame,previous_frame)
#    frame_diff = abs(current_frame-previous_frame)
    
    cv2.imshow('frame diff ',frame_diff)    
    
# tab 'ESC'
    key = cv2.waitKey(20) 
    if key == 27: # hadi hiyya Esc
        cap.release()
        cv2.destroyAllWindows()
        break
    
    previous_frame = current_frame.copy()
    ret, current_frame = cap.read()


