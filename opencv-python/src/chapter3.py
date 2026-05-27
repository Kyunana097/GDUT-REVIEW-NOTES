import cv2
import os

def empty(a):
    pass

print(cv2.__version__)
cv2.namedWindow("Bars")
cv2.resizeWindow("Bars",400,20)
cv2.createTrackbar("length","Bars",100,500,empty)

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, '..', 'assets', 'putin.png')

while True:
    img = cv2.imread(img_path)
    length = cv2.getTrackbarPos("length","Bars")
    imgResize = cv2.resize(img,(800,length))
    cv2.imshow("putin",imgResize)
    cv2.waitKey(1)