# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:28:58 2019

@author: maazouz
"""
import cv2
import numpy as np

cap = cv2.VideoCapture('../../Mh/highway.mp4')
count = 0
nb = 1
success = True
X_data = []

#point to test
p0 = np.array([[330, 445]], dtype=np.float32)

# Lucas kanade params
lk_params = dict(winSize = (15,15),
                 maxLevel = 4,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
#color = np.random.randint(0,255,(100,3))

while success:
    
    success,image = cap.read()
    
    if (count%13 == 0 and nb <= 2):
        print('read a new frame:',success)
#        cv2.imwrite("C:\\Users\\maazouz\\Desktop\\VA_ATELIER4\\" + 'frame%d.jpg'%nb,image)
        X_data.append (image)
        a,b = p0.ravel()
        frame1 = cv2.circle(image,(a,b),5,(0,0,255),-1)
        cv2.imshow('frame',image)
        nb+=1
        
    if nb == 3 :
        # Take first frame
        old_frame = X_data[0]
        old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
        
        # Create a mask image for drawing purposes
        mask = np.zeros_like(old_frame)
        frame = X_data[1]
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # calculate optical flow
        p1, status, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

        a,b = p0.ravel()
        c,d = p1.ravel()
        mask = cv2.line(mask,(a,b),(c,d),(255,0,255),4)
        frame1 = cv2.circle(frame,(a,b),5,(0,0,255),-1)
        frame1 = cv2.circle(frame,(c,d),5,(0,255,0),-1)
        img = cv2.add(frame1,mask)
        cv2.imshow('frame',img)
        nb+=1
        
    count+=1
    k = cv2.waitKey(20) & 0xff
    if (k == 27 or nb == 50):
        break
cap.release()
cv2.destroyAllWindows()