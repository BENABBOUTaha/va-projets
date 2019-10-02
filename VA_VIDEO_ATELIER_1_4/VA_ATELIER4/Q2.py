# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:02:26 2019

@author: maazouz
"""

import cv2
import numpy as np
cap = cv2.VideoCapture('../../Mh/highway.mp4')

# Create old frame
_, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# Lucas kanade params
lk_params = dict(winSize = (15, 15),
                 maxLevel = 4,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Mouse function
def select_point(event, x, y, flags, params):
    global point, point_selected, old_points
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        point_selected = True
        old_points = np.array([[x, y]], dtype=np.float32)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", select_point)
point_selected = False
point = ()
old_points = np.array([[]])
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
while True:
    _, new_frame = cap.read()
    gray_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
    
    if point_selected is True:
        new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **lk_params)
        a,b = new_points.ravel()
        c,d = old_points.ravel()
        mask = cv2.circle(mask,(a,b),4,(255,0,255),-1)
        new_frame = cv2.add(new_frame,mask)
        old_gray = gray_frame.copy()
        old_points = new_points       
    cv2.imshow("Frame", new_frame)
        
    key = cv2.waitKey(27)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()