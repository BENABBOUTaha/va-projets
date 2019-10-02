import cv2 as cv

I = cv.VideoCapture(0)
mogSubtractor = cv.bgsegm.createBackgroundSubtractorMOG()
while(1):
    _, frame = I.read()
    frame = cv.GaussianBlur(frame,(5,5),0)
    fgmask = mogSubtractor.apply(frame)

    cv.imshow('frame',frame)
    cv.imshow('fgmask',fgmask)

    
    k = cv.waitKey(20) & 0xff
    if k == 27:
        break
    

I.release()
cv.destroyAllWindows()