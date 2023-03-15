import cv2
import numpy as np

img = cv2.imread('../images/pyos-samolyot.jpg')

# """
# @param flipCode a flag to specify how to flip the array;
# 0 means
# .   flipping around the x-axis and positive value (for example,
# 1) means
# .   flipping around y-axis. Negative value (for example,
# -1) means flipping
# .   around both axes.
# """
# img = cv2.flip(src=img, flipCode=1)


def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (height // 2, width // 2)

    mat = cv2.getRotationMatrix2D(
        center=point,
        angle=angle,
        scale=1
    )

    return cv2.warpAffine(
        src=img_param,
        M=mat,
        dsize=(height, width)
    )

def transform(img_param, x, y):
    mat = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])

    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))


# img = rotate(img, 90)

img = transform(img, x=30, y=200)

cv2.imshow('Result', img)
cv2.waitKey(0)
