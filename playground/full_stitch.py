import cv2, glob, os

folder = "playground/testImg/fuji"
image_paths = sorted(glob.glob(os.path.join(folder, "*.png")))
imgs = [cv2.imread(p, cv2.IMREAD_COLOR) for p in image_paths]

stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
status, pano = stitcher.stitch(imgs)

if status == cv2.STITCHER_OK:
    cv2.imshow("Stitched Image", pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Stitching failed with code:", status)
