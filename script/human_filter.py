import glob, os
import cv2
import sys
import os.path

file = glob.glob("*.jpg")
img1 = cv2.imread(file[1], cv2.IMREAD_UNCHANGED)
img2 = cv2.imread(file[1], cv2.IMREAD_UNCHANGED)
img3 = cv2.imread(file[1], cv2.IMREAD_UNCHANGED)
img4 = cv2.imread(file[1], cv2.IMREAD_UNCHANGED)
img5 = cv2.imread(file[1], cv2.IMREAD_UNCHANGED)
state1 = False
state2 = False
state3 = False
state4 = False
state5 = False

for f in file:
    image = cv2.imread(f, cv2.IMREAD_UNCHANGED)
    print(f)
    cv2.imshow("-4",img1)
    cv2.imshow("-3",img2)
    cv2.imshow("-2",img3)
    cv2.imshow("-1",img4)
    cv2.imshow("0",img5)
    char = cv2.waitKey(0)
    print(char)
