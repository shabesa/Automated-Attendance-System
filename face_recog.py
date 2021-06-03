import face_recognition
import os
import cv2
import numpy as np

path = 'images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    currentImg = cv2.imread(f'{path}/{cl}')
    images.append(currentImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodedList = []
    for image in images:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encoded = face_recognition.face_encodings(img)[0]
        encodedList.append(encoded)
    return encodedList

encodedList = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    frame, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceLocInFrame = face_recognition.face_locations(imgS)
    encodeCurrentFrame = face_recognition.face_encodings(imgS, faceLocInFrame)

    for encodeFace, faceLoc in zip(encodeCurrentFrame, faceLocInFrame):
        matches = face_recognition.compare_faces(encodedList, encodeFace)
        faceDistance = face_recognition.face_distance(encodedList, encodeFace)
        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1 , (255, 255, 255), 2)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)