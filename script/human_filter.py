import glob, os
import cv2
import sys
import os.path

file = glob.glob("*.jpg")
img1 = cv2.imread(file[0], cv2.IMREAD_UNCHANGED)
img2 = cv2.imread(file[0], cv2.IMREAD_UNCHANGED)
img3 = cv2.imread(file[0], cv2.IMREAD_UNCHANGED)
img4 = cv2.imread(file[0], cv2.IMREAD_UNCHANGED)
img5 = cv2.imread(file[0], cv2.IMREAD_UNCHANGED)
state1 = False
state2 = False
state3 = False
state4 = False
state5 = False
name1 = file[0]
name2 = file[0]
name3 = file[0]
name4 = file[0]
name5 = file[0]

for f in file:
    image = cv2.imread(f, cv2.IMREAD_UNCHANGED)
    print(f)
    if (state5) :
        os.remove(name5)
    state5 = state4
    name5 = name4
    img5 = img4
    state4 = state3
    name4 = name3
    img4 = img3
    state3 = state2
    name3 = name2
    img3 = img2
    state2 = state1
    name2 = name1
    img2 = img1
    state1 = False
    name1 = f
    img1 = image
    cv2.imshow("-4",img5)
    cv2.imshow("-3",img4)
    cv2.imshow("-2",img3)
    cv2.imshow("-1",img2)
    cv2.imshow("0",img1)
    # Space : 32
    # Enter : 13
    while(True):
        char = cv2.waitKey(0)
        if (char == 13):
            state3 = True
            break
        elif (char == 32):
            state3 = False
            break
        elif (char == 3):
            exit()
        else:
            print("Unknown Command!")

