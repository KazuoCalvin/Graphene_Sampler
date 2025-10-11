import cv2
import numpy as np

img = cv2.imread('playground/testImg/5x_test.jpeg')

# Get image dimensions
height, width = img.shape[:2]

# Crop left 2/3 of the image
crop_width_left = int(width * 2/3)
img_left_2_3 = img[0:height, 0:crop_width_left]

# Crop right 2/3 of the image
# Start from 1/3 position and go to the end
start_x_right = int(width * 1/3)
img_right_2_3 = img[0:height, start_x_right:width]


imgs = [img_left_2_3, img_right_2_3]

stitcher = cv2.Stitcher.create(cv2.Stitcher_SCANS)
status, pano = stitcher.stitch(imgs)

cv2.imshow("Stitched Image", pano)
cv2.waitKey(0)
cv2.destroyAllWindows()