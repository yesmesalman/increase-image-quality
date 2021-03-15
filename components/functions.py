import cv2 as cv


def resize_image(image, dimensions, interpolation=cv.INTER_CUBIC):
    return cv.resize(image, dimensions, interpolation=interpolation)