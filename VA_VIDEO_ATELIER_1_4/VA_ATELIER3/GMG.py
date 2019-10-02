import cv2 as cv

I = cv.VideoCapture(0)
nb_frames = 30   # number of frames used to initialize the background models
de_th = 0.9 # Threshold value, above which it is marked foreground, else background.
gmgSubtractor = cv.bgsegm.createBackgroundSubtractorGMG(nb_frames,de_th)
while(1):
    ret, frame = I.read()
    frame = cv.GaussianBlur(frame,(5,5),0)
    fgmask = gmgSubtractor.apply(frame)

    cv.imshow('frame',frame)
    cv.imshow('fgmask',fgmask)

    
    k = cv.waitKey(20) & 0xff
    if k == 27:
        break
    

I.release()
cv.destroyAllWindows()