import glob, os
import cv2
import sys
import os.path

# os.chdir("../blhx (done)")
file = glob.glob("*.jpg")
cascade_file = "./lbpcascade_animeface.xml"
if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)
count = 0
for f in file:
    cascade = cv2.CascadeClassifier(cascade_file)
    # image = cv2.imread(f, cv2.IMREAD_COLOR)
    image = cv2.imread(f, cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    W,H,C = image.shape
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))
    print(f)
    for (x, y, w, h) in faces:
        x = x - int(float(w) * 1.2 / 2)
        y = y - int(float(h) * 1.2 / 2)
        w = int(w * 2.2)
        h = int(h * 2.2)
        if x < 0: 
            x = 0
        if y < 0:
            y = 0
        if x + w > W:
            w = W - x
        if y + h > H:
            h = H - y
        out = image[y:y+h,x:x+w,:]
        count += 1
        fileName = "./face/" + str(count) + ".jpg"
        try:
            cv2.imwrite(fileName,out)
        except:
            count -= 1

        