import tkinter
import pyttsx3
import json
from tkinter import *
from tkinter.constants import BOTTOM
from audio import AudioEngine

audioEngine = AudioEngine(pyttsx3.init('sapi5'), 0)

def IntroUI():
    body1 = tkinter.Tk()

    introLabel = tkinter.Label(master=body1, text="""Welcome to Automated Attendance System. Use start to activate the system. Click ok to continue.""", width=75)
    okButton = tkinter.Button(master=body1, text="OK", width=15, command=body1.destroy)
    introLabel.pack()
    okButton.pack(side=BOTTOM)
    body1.mainloop()

def MainUI():

    fileRead = open("settings.txt", "r", encoding="utf-8")
    settings = json.load(fileRead)
    fileRead.close()

    grade = settings['class']
    section = settings['section']
    
    def startButtonFunc():
        audioEngine.speak("Starting camera")
        startButton['state'] = DISABLED
        stopButton['state'] = NORMAL
        
    def stopButtonFunc():
        audioEngine.speak("Stopping camera")
        startButton['state'] = NORMAL
        stopButton['state'] = DISABLED
    
    body2 = tkinter.Tk()

    labelHeading = tkinter.Label(master=body2, text="Automated Attendance System", width=30)
    labelClass = tkinter.Label(master=body2,  text=f'{grade}-{section}')
    startButton = tkinter.Button(master=body2, text="Start", width=15, command=startButtonFunc, state=NORMAL)
    stopButton = tkinter.Button(master=body2, text="Stop", width=15, command=stopButtonFunc, state=DISABLED)

    labelHeading.pack(side=tkinter.TOP)
    labelClass.pack()
    startButton.pack(side=tkinter.LEFT)
    stopButton.pack(side=tkinter.LEFT)
    body2.mainloop()
