# face detection for image

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('blake.jpg')
#img = cv2.imread('sognsvann.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.2, 4)

print(faces)

# faces gives the coordinates of the image read
# scale factor - reduces the size of the image so that the processing will be faster
#faces = face_cascade.detectMultiScale(img)

if faces is ():
    print("No faces found")
# condition for no faces detection

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+h, y+h), (255, 0, 0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
