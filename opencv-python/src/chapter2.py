import cv2
import os

print(cv2.__version__)

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, '..', 'assets', 'lena.png')

img = cv2.imread(img_path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
imgCanny = cv2.Canny(imgBlur,100,100)

if img is None:
    print(f"Failed to load image: {img_path}")
else:
    cv2.imshow('Lena', img)
    cv2.imshow('LenaGray', imgGray)
    cv2.imshow('LenaBlur', imgBlur)
    cv2.imshow('LenaCanny', imgCanny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()