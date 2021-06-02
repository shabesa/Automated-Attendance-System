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

    if first_use == True:
        IntroUI()
        settings['checks']['first'] = False
        file = open('settings.txt', 'w')
        json.dump(settings, file)
        file.close()
    else:
        MainUI()
    
def IntroUI():
    body1 = tkinter.Tk()

    introLabel = tkinter.Label(master=body1, text="""Welcome to Automated Attendance System. Use start to activate the system. Click ok to continue.""", width=30)
    okButton = tkinter.Button(master=body1, text="OK", width=15, command=MainUI())

    introLabel.pack()
    okButton.pack(side=BOTTOM)
    body1.mainloop()

def MainUI():

        body2 = tkinter.Tk()
        labelHeading = tkinter.Label(master=body2, text="Automated Attendance System", width=30)
        startButton = tkinter.Button(master=body2, text="Start", width=15)
        stopButton = tkinter.Button(master=body2, text="Stop", width=15)

        labelHeading.pack(side=tkinter.TOP)
        startButton.pack(side=tkinter.LEFT)
        stopButton.pack(side=tkinter.LEFT)
        body2.mainloop()


if __name__=="__main__":
    checkJSON()