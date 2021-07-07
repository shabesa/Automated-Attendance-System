import tkinter
import json
import datetime
from tkinter import *
from tkinter.constants import BOTTOM
from audio import AudioEngine
from face_recog import *
from mail import SendMail

class UI:

    def __init__(self):
        self.audioEngine = AudioEngine(0)
        self.recogEngine = FaceRecog()
        self.audioEngine.speak("Encoding face into models")
        self.encodedList = self.recogEngine.findEncodings()
        self.audioEngine.speak("Encoding complete")

    #Provides intro of the project
    def IntroUI(self):
        body1 = tkinter.Tk()
        body1.title("Welcome")
        body1.resizable(False, False)

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
                    SendMail()

        
        body2 = tkinter.Tk()
        body2.geometry("910x100")
        body2.title('Automated Attendance System')
        body2.resizable(False, False)

        labelHeading = tkinter.Label(master=body2, text="Automated Attendance System", width=30)
        labelHeading.place(relx=0.375, rely=0.1)

        labelClass = tkinter.Label(master=body2,  text=f'{grade}-{section}')
        labelClass.place(relx=0.475, rely=0.3)

        startButton = tkinter.Button(master=body2, text="Start", width=15, command=startButtonFunc, state=NORMAL)
        startButton.place(relx=0.4315, rely=0.5)

        lastRunLabel = tkinter.Label(master=body2, text=f'Last Run: {lastRun}')
        lastRunLabel.place(relx=0.4085, rely=0.8)

        body2.mainloop()