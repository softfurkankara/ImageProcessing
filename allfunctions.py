import cv2
import numpy as np

def findOfCircle(frame):
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gri,(5,5),0)
    canny=cv2.Canny(blur,50,80)
    canny=cv2.bitwise_and(gri,gri,mask=canny)
    kernel=np.ones((5,5))
    dilate=cv2.dilate(canny,kernel,iterations=1)
    erosion=cv2.erode(dilate,kernel,iterations=1)
    kopya=erosion.copy()
    konturlar=cv2.findContours(kopya,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for cnt in konturlar:
        area=cv2.contourArea(cnt)

        

        if area>1000 and area<30000:#Birden fazla dikdörtgen bulma durumunda burayı arttır. Alan Büyüdükçe dikdörtgen azalıcak.
        
            x,y,w,h= cv2.boundingRect(cnt)
            genislik=int(w)
            uzunluk=int(h)
            oran=float(genislik/uzunluk)
            #if oran>1.4 and oran<2.1 or oran<1.6 and oran>1.4:

          
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            merkezx=int(x+w/2)
            merkezy=int(y+h/2)
            cv2.circle(frame,(merkezx,merkezy),1,(0,255,255),2)
    
    return frame,erosion,dilate,blur


def divideOfScreen(frame):
    cv2.line(frame,(320,0),(320,480),(0,255,255),1)
    cv2.line(frame,(0,240),(640,240),(0,255,255),1)
    return frame





    
    