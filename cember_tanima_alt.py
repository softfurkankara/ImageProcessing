
"""
Arkadaşlar, Hough Circles algoritmasıyla çember tanıyabileceğimiz bir alternatif yöntem.
Deneyebileceğiniz bazı paramatreler ve örnek değerler:
    - medianBlur yerine direk (3x3) ya da (5x5) kernel ile 'blur' fonksiyonunu deneyebilirsiniz. (18. satır)
    - param1 değeri: Canny edge detektörü için üst threshold değeri.(Çok arttırısanız program yavaşlar ve çökebilir eğer çok 
        azaltırsanız ise Edge detector beklenen performansı veremez. Kendim deneyerek en optimal değerin 100 olduğunu gördüm. (24. satır)
    -param2 parametresi: Center detektörü için threshold değeri. 
    -minRadius parametresi: Yakalanması gereken minimum radius değeri, verilmezse default olarak 0 atanır.
    -maxRadius parametresi: Yakalanması gereken maximum radius değer, verilmezse default olarak 0 atanır.
    -cv2.HOUGH_GRADIENT: Bu bizim tespit etme için kullanacagımız algoritma. Şu anda OpenCV'deki tek mevcut algoritma.


    daha fazla bilgi için buradan HOUGH_GRADIENT parametrelerine bakabilirsiniz:https://docs.opencv.org/3.4/dd/d1a/group__imgproc__feature.html#ga47849c3be0d0406ad3ca45db65a25d2d
"""
import cv2
import numpy as np

capture = cv2.VideoCapture(0)


while True:
    goon, frame = capture.read()
    capture_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    capture_gray_blurred = cv2.medianBlur(capture_gray, 5)

    rows = capture_gray_blurred.shape[0]
  
    detected_circles = cv2.HoughCircles(capture_gray_blurred, 
                   cv2.HOUGH_GRADIENT, 1, rows / 8, param1 = 100,
               param2 = 30, minRadius = 1, maxRadius = 40)
  

    if detected_circles is not None:
    
        
        detected_circles = np.uint16(np.around(detected_circles))
    
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
    
            
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
    
            
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)
            cv2.imshow("Detected Circle", frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.DestroyAllWindows()