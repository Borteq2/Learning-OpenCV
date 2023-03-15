import cv2

img = cv2.imread('../images/file_50684_258710.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(
    image=gray,
    scaleFactor=1.2,
    minNeighbors=2
)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv2.imshow('Result', img)
cv2.waitKey(0)
