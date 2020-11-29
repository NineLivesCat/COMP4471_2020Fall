import cv2
import sys
import os.path

def PNGtoJPG(filename, treshold):
    if not os.path.isfile(filename):
        return None
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    W,H,C = img.shape
    
    # out = cv2.createMat(W, H, cv2.CV_8UC3)
    for i in range(W):
        for j in range(H):
            if img[i,j,3] < treshold:
                img[i,j,:] = [255,255,255,0]
    img = img[:,:,0:3]
    cv2.imshow("test",img)
    cv2.waitKey(0)

# def detect(filename, cascade_file = "../lbpcascade_animeface.xml"):
#     if not os.path.isfile(cascade_file):
#         raise RuntimeError("%s: not found" % cascade_file)

#     cascade = cv2.CascadeClassifier(cascade_file)
#     # image = cv2.imread(filename, cv2.IMREAD_COLOR)
#     image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     gray = cv2.equalizeHist(gray)
    
#     faces = cascade.detectMultiScale(gray,
#                                      # detector options
#                                      scaleFactor = 1.1,
#                                      minNeighbors = 5,
#                                      minSize = (24, 24))
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

#     cv2.imshow("AnimeFaceDetect", image)
#     cv2.waitKey(0)
#     cv2.imwrite("out.png", image)

if len(sys.argv) != 2:
    sys.stderr.write("usage: detect.py <filename>\n")
    sys.exit(-1)
    
PNGtoJPG(sys.argv[1],80)
