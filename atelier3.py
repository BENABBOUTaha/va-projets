# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:48:19 2019

@author: mhmh2
"""

import cv2
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('C:/Users/mhmh2/Downloads/Video/musicDance.mp4')

MOG2 = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)
#subtractor2 = cv2.bgsegm.createBackgroundSubtractorMOG()
KNN	=	cv2.createBackgroundSubtractorKNN(history=20, dist2Threshold=10, detectShadows=True)

while True:
    ret, frame = cap.read()
    
    frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)
    frame = cv2.flip(frame, 1)
    cv2.moveWindow('Frame',700,10)
    
    maskMOG2 = MOG2.apply(frame)
    
    cv2.moveWindow('Mask MOG2',10,10)
    
    maskKNN = KNN.apply(frame)
    cv2.moveWindow('Mask KNN',10,350)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask MOG2", maskMOG2)
    cv2.imshow("Mask KNN", maskKNN)

    key = cv2.waitKey(20) 
    if key == 27: # hadi hiyya Esc
        cap.release()
        cv2.destroyAllWindows()
        break


