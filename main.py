import os
import json
import face_recognition
import cv2
import tkinter
from tkinter.constants import BOTTOM, CENTER, LEFT

def checkJSON():
    fileRead = open("settings.txt", "r", encoding="utf-8")
    settings = json.load(fileRead)
    fileRead.close()

    first_use = settings['checks']['first']
    #print(first_use)

    if first_use == True:
        UI(first_use)
        settings['checks']['first'] = False
        file = open('settings.txt', 'w')
        json.dump(settings, file)
        file.close()
    else:
        UI(first_use)
  

def UI(method):

        body = tkinter.Tk()
        labelHeading = tkinter.Label(master=body, text="Automated Attendance System", width=30)
        startButton = tkinter.Button(master=body, text="Start", width=15)
        stopButton = tkinter.Button(master=body, text="Stop", width=15)

        labelHeading.pack(side=tkinter.TOP)
        startButton.pack(side=tkinter.LEFT)
        stopButton.pack(side=tkinter.LEFT)
        body.mainloop()


if __name__=="__main__":
    checkJSON()