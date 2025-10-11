import cv2
import numpy as np

img = cv2.imread('playground/testImg/5x_test.jpeg', cv2.IMREAD_GRAYSCALE)

# Get image dimensions
height, width = img.shape[:2]

# Crop left 2/3 of the image
crop_width_left = int(width * 2/3)
img_left_2_3 = img[0:height, 0:crop_width_left]

# Crop right 2/3 of the image
# Start from 1/3 position and go to the end
start_x_right = int(width * 1/3)
img_right_2_3 = img[0:height, start_x_right:width]

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
keypoints_left, descriptors_left = sift.detectAndCompute(img_left_2_3, None)
keypoints_right, descriptors_right = sift.detectAndCompute(img_right_2_3, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptors_left, descriptors_right, k=2)

# Apply ratio test to filter good matches
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

pts_left  = np.float32([keypoints_left[m.queryIdx].pt  for m in good_matches]).reshape(-1,1,2)
pts_right = np.float32([keypoints_right[m.trainIdx].pt for m in good_matches]).reshape(-1,1,2)

# Estimate homography that maps RIGHT -> LEFT
H, inlier_mask = cv2.findHomography(pts_right, pts_left, cv2.RANSAC, 4.0)