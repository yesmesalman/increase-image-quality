import cv2 as cv
from components import functions



image = cv.imread('input/images/house.tif')
reszed = functions.resize_image(image, (250, 250))
cv.imshow('image', reszed)

cv.waitKey(0)