import cv2
import math
import numpy as np
import sys

def apply_mask(matrix, mask, fill_value):
    masked = np.ma.array(matrix, mask=mask, fill_value=fill_value)
    return masked.filled()

def apply_threshold(matrix, low_value, high_value):
    low_mask = matrix < low_value
    matrix = apply_mask(matrix, low_mask, low_value)

    high_mask = matrix > high_value
    matrix = apply_mask(matrix, high_mask, high_value)

    return matrix

def simplest_cb(img, percent):
    assert img.shape[2] == 3
    assert percent > 0 and percent < 100
    half_percent = percent / 200.0
    channels = cv2.split(img)

    out_channels = []
    for channel in channels:
        assert len(channel.shape) == 2
        # [EN] find the low and high precentile values (based on the input percentile)
        # [TR] düşük ve yüksek yüzdelik değerleri girdiye göre buluyoruz
        height, width = channel.shape
        vec_size = width * height
        flat = channel.reshape(vec_size)

        assert len(flat.shape) == 1
        flat = np.sort(flat)
        n_cols = flat.shape[0]

        low_val  = flat[math.floor(n_cols * half_percent)]
        high_val = flat[math.ceil( n_cols * (1.0 - half_percent))]

        # [EN] saturate below the low percentile and above the high percentile
        # [TR] düşük yüzdeliğin altında ve yüksek yüzdeliğin üstünde doygunluk elde ediyoruz
        thresholded = apply_threshold(channel, low_val, high_val)

        # [EN] scale the channel
        # [TR] ölçeklendiriyoruz
        normalized = cv2.normalize(thresholded, thresholded.copy(), 0, 255, cv2.NORM_MINMAX)
        out_channels.append(normalized)

    return cv2.merge(out_channels)

video=cv2.VideoCapture(r'C:\Users\frknl\Desktop\Teknofest\img\video\sualti.mp4')

while True:
    ret,frame=video.read()
    medianBlur=cv2.medianBlur(frame,7)
    gaussianBlur=cv2.GaussianBlur(frame,(5,5),0)
    frame=cv2.resize(frame,(600,600),2,2,cv2.INTER_AREA)
    out = simplest_cb(gaussianBlur, 1)
    cv2.imshow("before", frame)
    cv2.imshow("after", out)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()

    
