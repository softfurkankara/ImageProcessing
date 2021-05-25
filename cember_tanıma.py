import cv2
import math

cap = cv2.VideoCapture(0)

while 1:
    ret, raw_image = cap.read()
    raw_image = cv2.flip(raw_image, 1)
    bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)

    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)

    contours, _  = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 12) & (len(approx) < 23) & (area > 40)):
            if ((len(approx) > 12) & (len(approx) < 23) & (area > 20)):
                r=math.sqrt(area/3.14)
                M = cv2.moments(contour)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.putText(raw_image, ".", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 5)
                cv2.circle(raw_image,(cX,cY),int(r),(0,0,255),4)
                contour_list.append(contour)

    #cv2.drawContours(raw_image, contour_list, -1, (255, 0, 0), 2)
    cv2.imshow('Objects Detected', raw_image)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()