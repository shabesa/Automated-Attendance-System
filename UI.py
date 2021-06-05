import tkinter
import pyttsx3
import json
import datetime
from tkinter import *
from tkinter.constants import BOTTOM
from audio import AudioEngine
from face_recog import *

class UI:

    def __init__(self):
        self.audioEngine = AudioEngine(pyttsx3.init('sapi5'), 0)
        self.recogEngine = FaceRecog()
        self.audioEngine.speak("Encoding face into models")
        self.encodedList = self.recogEngine.findEncodings()
        self.audioEngine.speak("Encoding complete")

    #Provides intro of the project
    def IntroUI(self):
        body1 = tkinter.Tk()

        introLabel = tkinter.Label(master=body1, text="""Welcome to Automated Attendance System. Use start to activate the system. Click ok to continue.""", width=75)
        okButton = tkinter.Button(master=body1, text="OK", width=15, command=body1.destroy)
        introLabel.pack()
        okButton.pack(side=BOTTOM)
        body1.mainloop()

    #The main UI with controls 
    def MainUI(self):

        #Reading json file for settings
        fileRead = open("settings.txt", "r", encoding="utf-8")
        settings = json.load(fileRead)
        fileRead.close()

        grade = settings['class']
        section = settings['section']
        lastRun = settings['checks']['lastrun']
        
        #Function for the start button 
        def startButtonFunc():
                control = True
                self.audioEngine.speak("Starting recognition")
                control = self.recogEngine.recogVideo(self.encodedList, control)
                
                #Writing the last use time 
                if control == False:
                    self.audioEngine.speak("Stopping recognition")
                    now = datetime.now()
                    last = now.strftime("%d-%m-%y, %H:%M:%S")
                    settings['checks']['lastrun'] = last
                    file = open('settings.txt', 'w')
                    json.dump(settings, file)
                    file.close()
                    lastRunLabel.config(text=f'Last Run: {last}')

        
        body2 = tkinter.Tk()

        labelHeading = tkinter.Label(master=body2, text="Automated Attendance System", width=30)
        labelClass = tkinter.Label(master=body2,  text=f'{grade}-{section}')
        startButton = tkinter.Button(master=body2, text="Start", width=15, command=startButtonFunc, state=NORMAL)
        lastRunLabel = tkinter.Label(master=body2, text=f'Last Run: {lastRun}')

        labelHeading.pack(side=tkinter.TOP)
        labelClass.pack()
        startButton.pack()
        lastRunLabel.pack(side=tkinter.BOTTOM)
        body2.mainloop()
