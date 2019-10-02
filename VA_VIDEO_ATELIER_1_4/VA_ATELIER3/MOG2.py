import cv2 as cv

I = cv.VideoCapture(0)
fgbg = cv.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = I.read()
    frame = cv.GaussianBlur(frame,(5,5),0)
    fgmask = fgbg.apply(frame)
    cv.imshow('frame',frame)
    cv.imshow('fgmask',fgmask)

    
    k = cv.waitKey(20) & 0xff
    if k == 27:
        break
    

I.release()
cv.destroyAllWindows()