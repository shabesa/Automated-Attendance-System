import face_recognition
import os
import cv2
import numpy as np
from datetime import datetime

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

def markAttendance(name):
    with open('attendance.csv', 'r+') as file:
        myDataList = file.readlines()
        nameList=[]
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            file.writelines(f'\n{name},{dtString}')

encodedList = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    frame, img = cap.read()
    #imgS = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

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
            #y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1 , (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)