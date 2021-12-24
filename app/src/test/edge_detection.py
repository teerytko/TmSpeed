#!/usr/bin/python3
#
import os
import cv2
import numpy as np
 

curdir = os.path.dirname(__file__)


def main():
    # Creating a VideoCapture object to read the video
    cap = cv2.VideoCapture(os.path.join(curdir, 'matto_teipilla.mp4'))
    font = cv2.FONT_HERSHEY_SIMPLEX
    prevpos = None
    rotation = 0
    rotation_ts = []
    speed = 0
    matlength = 300
    while (cap.isOpened()):
        
        # Capture frame-by-frame
        ret, frame = cap.read()
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
        pos = []
        if ret:
            frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,
                                interpolation = cv2.INTER_CUBIC)
            heigh, widht, _ = frame.shape
            midheigh = int(heigh / 2)
            midwidth = int(widht / 2)
            # conversion of BGR to grayscale is necessary to apply this operation
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Blur the image for better edge detection
            img_blur = cv2.GaussianBlur(gray, (3,3), 0) 
            # Canny Edge Detection
            edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
            # find the line pos
            a = np.asarray(edges)
            for i in range(widht):
                if a[midheigh][i] > 0:
                    pos.append(i)
            
            # detect moving line
            movingline = None
            if prevpos:
                for i in range(len(prevpos)):
                    if i < len(pos):
                        if pos[i] == prevpos[i]:
                            continue
                        elif (prevpos[i] - pos[i]) > 5:
                            # moving line
                            movingline = pos[i]
                            cv2.line(frame, (movingline, 0), (movingline, heigh), (255, 0,0), 2)
                            if prevpos[i] > midwidth and pos[i] < midwidth:
                                rotation_ts.append(timestamp)
                                rotation += 1
                            break
            if len(rotation_ts) >= 2:
                # rotation time seconds
                rotation_time = (rotation_ts[rotation-1] - rotation_ts[rotation-2]) / 1000
                # speed m/s
                speed_ms = (matlength / 100) / rotation_time
                # speed km/h
                speed = speed_ms * 3.6
                        
            cv2.line(frame, (midwidth, 0), (midwidth, heigh), (0, 255,0), 2)
            cv2.putText(frame,'ts: %.2f' % timestamp,(20,30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(frame,'rotation: %s' % rotation,(20,60), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(frame,'speed: %.3f' % speed,(20,90), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            #cv2.imshow('Canny Edge Detection', edges)

            # define q as the exit button
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            prevpos = pos
        else:
            break
    
    # release the video capture object
    cap.release()
    # Closes all the windows currently opened.
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()