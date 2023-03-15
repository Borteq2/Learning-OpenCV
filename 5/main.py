import cv2

img = cv2.imread('../images/pyos-samolyot.jpg')

# img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2HSV)
img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(src=img, code=cv2.COLOR_LAB2BGR)
img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

img = cv2.merge([r, g, b])
cv2.imshow(
    winname='Result',
    mat=img  # or g or b
)

cv2.waitKey(0)
