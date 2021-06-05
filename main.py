import os
import json
import pyttsx3
from audio import AudioEngine
from UI import UI

audioEngine = AudioEngine(pyttsx3.init('sapi5'), 0)
GUIs = UI()

def checkJSON():
    fileRead = open("settings.txt", "r", encoding="utf-8")
    settings = json.load(fileRead)
    fileRead.close()

    first_use = settings['checks']['first']

    if first_use == True:
        GUIs.IntroUI()
        settings['checks']['first'] = False
        file = open('settings.txt', 'w')
        json.dump(settings, file)
        file.close()
        os.system('python "E:\\shabesa\\Projects\\Shabesa\\Automated-Attendance-System\\main.py"')
    if first_use == False:
        GUIs.MainUI()

if __name__=="__main__":
    checkJSON()