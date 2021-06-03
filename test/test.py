import face_recognition
from face_recognition.api import face_distance
import numpy as np
import cv2

imgRDJ = face_recognition.load_image_file('E:\\shabesa\\Projects\\Shabesa\\Automated-Attendance-System\\test\\images\\rdj2.jpg')
imgRDJ = cv2.cvtColor(imgRDJ, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('E:\\shabesa\\Projects\\Shabesa\\Automated-Attendance-System\\test\\images\\rdj1.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgRDJ)[0]
encodeRDJ = face_recognition.face_encodings(imgRDJ)[0]
cv2.rectangle(imgRDJ, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 0, 255), 2)

result = face_recognition.compare_faces([encodeRDJ], encodeTest)
faceDis = face_recognition.face_distance([encodeRDJ], encodeTest)
print(result, faceDis)

cv2.imshow('RDJ', imgRDJ)
cv2.imshow('RDJ Test', imgTest)
cv2.waitKey(0)