import glob, os
import cv2
import sys
import os.path

def PNGtoJPG(filename, treshold):
    if not os.path.isfile(filename):
        return None
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    W,H,C = img.shape
    for i in range(W):
        for j in range(H):
            if img[i,j,3] < treshold:
                img[i,j,:] = [255,255,255,0]
    img = img[:,:,0:3]
    return img

# os.chdir("../blhx (done)")
file = glob.glob("*.*")
for f in file:
    out = PNGtoJPG(f,80)
    if out is not None:
        cv2.imwrite("./blhx(washed)/" + f,out)