import cv2


def main():
    img = cv2.imread('images/photo_2023-01-19_23-00-58.jpg')
    cv2.imshow('Result', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()