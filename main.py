import cv2


def read_show_photo(path='images/pyos-samolyot.jpg'):
    img = cv2.imread(path)

    # new_img = cv2.resize(img, (300, 500))  # cruel resizing
    img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))  # proportional resizing
    img = cv2.GaussianBlur(img, (9, 9), 0)  # only not odd values in tuple


    print(img.shape)  # width height layers
    cv2.imshow('Result', img) # whole pic
    # cv2.imshow('Result', img[0:100, 0:150]) # croping
    cv2.waitKey(0)


def read_show_video(path='videos/16788634373451.mp4'):
    cap = cv2.VideoCapture(path)

    while True:
        success, img = cap.read()
        cv2.imshow('Result', img)

        if cv2.waitKey(1) & 0xFF == ord('q') : # necessary for working, 1 is minimal value, q is break cycle key, can use any
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
    read_show_photo()


if __name__ == '__main__':
    main()