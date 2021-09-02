# -*- coding: UTF-8 -*-
from data_map import DataMapper
from SerialComms import SerialComms
import face_recognition
import os
import cv2
import numpy as np
from datetime import datetime
import csv
from time import sleep
from audio import AudioEngine
from firebase import UpdateBase

class FaceRecog:

    #Appending the images from the path and creating the attendance file
    def __init__(self):
        self.path = 'images'
        self.images = []
        self.classNames = []
        self.myList = os.listdir(self.path)
        self.board1 = SerialComms('COM12', 9600)
        # self.board2 = SerialComms('COM7', 9600)
        self.audioEngine = AudioEngine(0)
        self.fireBase = UpdateBase()
        print(self.myList)
        for cl in self.myList:
            currentImg = cv2.imread(f'{self.path}/{cl}')
            self.images.append(currentImg)
            self.classNames.append(os.path.splitext(cl)[0])
        print(self.classNames)

        #Preventing duplication of files
        self.now = datetime.now()
        self.fileName = self.now.strftime('%d-%m-%Y')
        self.month = self.now.strftime('%B')
        if self.month not in os.listdir('attendance'):
            os.makedirs(f'attendance/{self.month}')
            if f'{self.fileName}.csv' not in os.listdir(f'attendance/{self.month}'):
                with open(f'attendance/{self.month}/{self.fileName}.csv', 'w') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Name", "Time", "Status", "Verification"])
        
        elif self.month in os.listdir('attendance'):
            with open(f'attendance/{self.month}/{self.fileName}.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Time", "Status", "Verification"])
            
        #reading the cards file
        with open('cards.csv', 'r') as cfile:
            myC_Data = cfile.readlines()
            self.cardsDict = {}
            self.cardsList = []
            for line in myC_Data:
                entry = line.split(',')
                card = entry[1].splitlines()
                self.cardsDict[card[0]] = entry[0]
                self.cardsList.append(card[0])
            print(self.cardsDict)

    #Finding the encodings of the faces in the images 
    def findEncodings(self):
        encodedList = []
        for image in self.images:
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            encoded = face_recognition.face_encodings(img)[0]
            encodedList.append(encoded)
        print('Encoding Complete')
        return encodedList
    
    #Marks the attendance into a csv file
    def markAttendance(self, name):
        
        # opening csv file with UTF-8 support
        with open(f'attendance/{self.fileName}.csv', 'r+', encoding='UTF-8') as file:
            myDataList = file.readlines()
            nameList=[]
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            val_send = name.split(' ')
            # self.board2.write(val_send[0])
            sleep(5)
            data = self.board1.read().splitlines()
            print(data[0])

            #matching the data with rfid
            if name not in nameList and data[0] in self.cardsList:
                # finding students rfid and marking attendance
                if self.cardsDict[data[0]] == name:
                    print('normal')
                    fileNow= datetime.now()
                    dtString = fileNow.strftime('%H:%M:%S')
                    
                    # checking time limit 
                    if dtString <= '08:00:00':
                        file.writelines(f"\n{name},{dtString},On Time,✔")
                        self.fireBase.addData(self.fileName, name, dtString, u'student', u'On Time')
                    else:
                        file.writelines(f"\n{name},{dtString},Late,✔")
                        self.fireBase.addData(self.fileName, name, dtString, u'student', u'LLate')
                
                # using overide - teachers key to mark attendance of students with no rfid
                elif self.cardsDict[data[0]] == 'OVERIDE':
                    print('overide')
                    fileNow= datetime.now()
                    dtString = fileNow.strftime('%H:%M:%S')
                    
                    # checking time limit
                    if dtString <= '08:00:00':
                        file.writelines(f"\n{name},{dtString},On Time,❌")
                        self.fireBase.addData(self.fileName, name, dtString, u'Overide', u'On Time')
                    else:
                        file.writelines(f"\n{name},{dtString},Late,❌")
                        self.fireBase.addData(self.fileName, name, dtString, u'Overide', u'Late')
                
                # using cancel to ignore unwanted detection 
                elif self.cardsDict[data[0]] == 'CANCEL':
                    print('CANCEL')
                    return

                else:
                    self.audioEngine.speak(f'identified name {name} does not match with rfid {data[0]}')
                    print(f'identified name {name} does not match with rfid {data[0]}')
                    self.audioEngine.speak(f'the rfid {data[0]} is the student with name {self.cardsDict[data[0]]}')
                    print(f'the rfid {data[0]} is the student with name {self.cardsDict[data[0]]}')
                    self.audioEngine.speak('try again')
                    print('try again')

    #Starts the live camera for recognizing
    def recogVideo(self, encodedList, control):
        cap = cv2.VideoCapture(0)

        while control:
            frame, img = cap.read()
            #imgS = cv2.resize(img, (0, 0), None, 0.5, 0.5)
            imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            faceLocInFrame = face_recognition.face_locations(imgS)
            encodeCurrentFrame = face_recognition.face_encodings(imgS, faceLocInFrame)

            for encodeFace, faceLoc in zip(encodeCurrentFrame, faceLocInFrame):
                matches = face_recognition.compare_faces(encodedList, encodeFace)
                faceDistance = face_recognition.face_distance(encodedList, encodeFace)
                matchIndex = np.argmin(faceDistance)
                
                #Matching the encodings
                if matches[matchIndex]:
                    name = self.classNames[matchIndex] #.upper()
                    print(name)
                    y1, x2, y2, x1 = faceLoc
                    #y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 0, 255), cv2.FILLED)
                    cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1 , (255, 255, 255), 2)
                    self.markAttendance(name)

            cv2.imshow('Webcam', img)
            k = cv2.waitKey(30) & 0xff
            if k==27:
                control = False
        cv2.destroyAllWindows()           
        return control
