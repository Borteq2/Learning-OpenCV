import cv2
import numpy as np

img = cv2.imread('../images/pyos-samolyot.jpg')

new_img = np.zeros(img.shape, dtype='uint8')

img = cv2.cvtColor(
    src=img,
    code=cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(
    src=img,
    ksize=(5, 5),
    sigmaX=0
)

img = cv2.Canny(
    image=img,
    threshold1=50,
    threshold2=50
)

con, hir = cv2.findContours(
    image=img,
    mode=cv2.RETR_LIST,
    method=cv2.CHAIN_APPROX_NONE
)

cv2.drawContours(
    image=new_img,
    contours=con,
    contourIdx=-1,
    color=(230, 111, 148),
    thickness=1
)

cv2.imshow('Result', new_img)
cv2.waitKey(0)