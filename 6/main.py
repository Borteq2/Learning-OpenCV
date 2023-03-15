import cv2
import numpy as np

# photo = cv2.imread('../images/pyos-samolyot.jpg')
img = np.zeros((350, 350), dtype='uint8')

circle = cv2.circle(
    img=img.copy(),
    center=(0, 0),
    radius=50,
    color=255,
    thickness=-1,  # filled
)

square = cv2.rectangle(
    img=img.copy(),
    pt1=(25, 25),
    pt2=(250, 350),
    color=255,
    thickness=-1,  # filled
)

# img = cv2.bitwise_and(circle, square)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_xor(circle, square)
img = cv2.bitwise_not(circle)

# cv2.imshow('Result', circle)
# cv2.imshow('Result', square)
cv2.imshow('Result', img)
cv2.waitKey(0)
