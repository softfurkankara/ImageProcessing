import cv2
import numpy as np
import time
import allfunctions
import CommunicateMotor

video=cv2.VideoCapture(0)
lower_color=np.array([20,147,0])
upper_color = np.array([30,255,255])
while True:
    ret,frame=video.read()
    time.sleep(.05)
    frame=cv2.GaussianBlur(frame,(7,7),0)
    frame=cv2.resize(frame,(640,480),interpolation=cv2.INTER_CUBIC)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower_color,upper_color)
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    merkezx=0
    merkezy=0
    for cnt in contours:
        area  = cv2.contourArea(cnt)
            
        if area>3000 and area<30000:#Birden fazla dikdörtgen bulma durumunda burayı arttır. Alan Büyüdükçe dikdörtgen azalıcak.
            
            x,y,w,h = cv2.boundingRect(cnt)
            
            genislik=int(w)
            uzunluk=int(h)
            oran=float(genislik/uzunluk)
            
            if oran>1.7 and oran<2.1:

                
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                merkezx=int(x+w/2)
                merkezy=int(y+h/2)
                cv2.circle(frame,(merkezx,merkezy),1,(0,255,255),2)
                merkezx=merkezx-320
                merkezy=240-merkezy

                CommunicateMotor.communicateMotor(merkezx,merkezy)
    cv2.putText(frame,"X:"+str(merkezx),(500,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    cv2.putText(frame,"Y:  "+str(merkezy),(500,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)

    frame=allfunctions.divideOfScreen(frame)
    

    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)

    if k==27 or k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
