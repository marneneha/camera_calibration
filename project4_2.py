import numpy as np
from pprint import pprint
import cv2 as cv2
import glob

images = glob.glob('proj4/Calibration_Imgs/*.png')
frameSize = (1512,2688)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
chessboardSize = (8,5)
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)
print("m herr")
size_of_chessboard_squares_mm = 20
objp = objp * size_of_chessboard_squares_mm
for image in images:
    current_img = cv2.imread(image)
    gray = cv2.cvtColor(current_img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (8,5), None)
    print("m here")
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(current_img, chessboardSize, corners2, ret)
        cv2.imshow('img', current_img)
        cv2.waitKey(1000)


# cv2.destroyAllWindows()
# ret, cameraMatrix, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, frameSize, None, None)
# pprint(cameraMatrix)
# pprint(ret)