import cv2
import numpy as np
import imutils
import easyocr

from matplotlib import pyplot as pl

img = cv2.imread('../images/num4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(src=gray,
                                 d=11,
                                 sigmaColor=15,
                                 sigmaSpace=15
                                 )

edges = cv2.Canny(image=img_filter,
                  threshold1=30,
                  threshold2=200)

cont = cv2.findContours(image=edges.copy(),
                        mode=cv2.RETR_TREE,
                        method=cv2.CHAIN_APPROX_SIMPLE)

cont = imutils.grab_contours(cont)
cont = sorted(cont,
              key=cv2.contourArea,
              reverse=True)[:8]

pos = None
for c in cont:
    approx = cv2.approxPolyDP(curve=c,
                              epsilon=10,
                              closed=True)
    if len(approx) == 4:
        pos = approx
        break

mask = np.zeros(gray.shape,
                np.uint8)
new_img = cv2.drawContours(mask,
                           [pos],
                           0,
                           255,
                           -1)
bitwise_img = cv2.bitwise_and(img,
                              img,
                              mask=mask)

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
x2, y2 = (np.max(x), np.max(y))
crop = gray[x1:x2, y1:y2]

text = easyocr.Reader(['en'])
text = text.readtext(crop)

res = text[0][-2]
final_img = cv2.putText(img,
                    res,
                    (x1, y2+60),
                    cv2.FONT_HERSHEY_PLAIN,
                    3,
                    (0, 0, 255),
                    2)
final_img = cv2.rectangle(img, (x1, x2), (y1, y2), (0, 255, 0), 2)

# pl.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# pl.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
pl.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))
pl.show()
