import numpy as np
import cv2
font1= cv2.FONT_HERSHEY_COMPLEX
frame=cv2.imread(r'C:\Users\frknl\Desktop\Teknofest\img\yellowrectangle.png')
lower_color = np.array([0,0,0])
upper_color = np.array([0,255,255])
frame=cv2.GaussianBlur(frame,(5,5),0)
frame=cv2.resize(frame,(640,480),interpolation=cv2.INTER_CUBIC)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,lower_color,upper_color)
contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    area  = cv2.contourArea(cnt)
        
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)  
    
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    
    if area>1000 and area<30000:#Birden fazla dikdörtgen bulma durumunda burayı arttır. Alan Büyüdükçe dikdörtgen azalıcak.
        
        x,y,w,h = cv2.boundingRect(cnt)
        
        genislik=int(w)
        uzunluk=int(h)
        oran=float(genislik/uzunluk)
        if oran>1.8 and oran<2.1 or oran<1.6 and oran>1.4:

        
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            merkezx=int(x+w/2)
            merkezy=int(y+h/2)
            cv2.circle(frame,(merkezx,merkezy),1,(0,255,255),2)
        
        #print(str(genislik)+','+''+str(uzunluk))
        print(area,oran)
cv2.imshow('img',frame)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()