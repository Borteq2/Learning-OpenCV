import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

cv2.rectangle(photo, (50, 70), (100, 100), (119, 201, 105), thickness=cv2.FILLED)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (119, 201, 105), thickness=3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 100, (119, 201, 105), thickness=1)

cv2.putText(
    img=photo,
    text='Hello morzh',
    org=(100, 150),
    fontFace=cv2.FONT_HERSHEY_TRIPLEX,
    fontScale=1,
    color=(255, 0, 0),
    thickness=1
)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
