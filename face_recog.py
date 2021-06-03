import face_recognition
import os
import cv2
import numpy

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
        encoded = face_recognition.face_encodings(image)[0]
        encodedList.append(encoded)
    return encodedList

encodedList = findEncodings(images)
print(len(encodedList))


# faceLoc = face_recognition.face_locations(imgRDJ)[0]
# encodeRDJ = face_recognition.face_encodings(imgRDJ)[0]
# cv2.rectangle(imgRDJ, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 255), 2)

# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 0, 255), 2)

# result = face_recognition.compare_faces([encodeRDJ], encodeTest)
# faceDis = face_recognition.face_distance([encodeRDJ], encodeTest)
# print(result, faceDis)