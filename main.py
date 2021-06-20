import os
import json
from UI import UI

#init the other modules
GUIs = UI()

# reading the json file and starting the program
def Main():
    fileRead = open("settings.txt", "r", encoding="utf-8")
    settings = json.load(fileRead)
    fileRead.close()

    first_use = settings['checks']['first']

    #showing intro for the first use
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
    Main()