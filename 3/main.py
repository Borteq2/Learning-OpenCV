import cv2
import numpy as np


def read_show_photo(path='images/pyos-samolyot.jpg'):
    img = cv2.imread(path)

    # new_img = cv2.resize(img, (300, 500))  # cruel resizing
    img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))  # proportional resizing
    img = cv2.GaussianBlur(img, (1, 1), 0)  # only not odd values in tuple
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.Canny(img, 140, 140)  # lower = more precision

    kernel = np.ones((5, 5), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)  # around lines

    img = cv2.erode(img, kernel, iterations=1)

    print(img.shape)  # width height layers
    cv2.imshow('Result', img) # whole pic
    # cv2.imshow('Result', img[0:100, 0:150]) # croping
    cv2.waitKey(0)


def read_show_video(path='videos/16788634373451.mp4'):
    cap = cv2.VideoCapture(path)

    while True:
        success, img = cap.read()
        cv2.imshow('Result', img)

        img = cv2.GaussianBlur(img, (9, 9), 0)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.Canny(img, 30, 30)

        kernel = np.ones((5, 5), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)

        cv2.imshow('Result', img)

        if cv2.waitKey(10) & 0xFF == ord('q'):  # necessary for working, 1 is minimal value, 10 better, q is break cycle key, can use any
            break




def read_show_webcam(path=0):  # 0 is list index for webcams (if many than 1)
    cap = cv2.VideoCapture(path)
    cap.set(3, 500)  # 3 is width
    cap.set(4, 300)  # 4 is height

    while True:
        success, img = cap.read()
        cv2.imshow('Result', img)

        if cv2.waitKey(1) & 0xFF == ord('q') : # necessary for working, 1 is minimal value, q is break cycle key, can use any
            break


def main():
    read_show_video()


if __name__ == '__main__':
    main()