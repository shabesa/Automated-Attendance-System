import os
import json
import face_recognition
import cv2
import pyttsx3
import tkinter
from tkinter import *
from tkinter.constants import BOTTOM
from audio import AudioEngine

audioEngine = AudioEngine(pyttsx3.init('sapi5'), 0)

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
        os.system('python "E:\\shabesa\\Projects\\Shabesa\\Automated-Attendance-System\\main.py"')
    if first_use == False:
        MainUI()

def IntroUI():
    body1 = tkinter.Tk()

    introLabel = tkinter.Label(master=body1, text="""Welcome to Automated Attendance System. Use start to activate the system. Click ok to continue.""", width=75)
    okButton = tkinter.Button(master=body1, text="OK", width=15, command=body1.destroy)
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