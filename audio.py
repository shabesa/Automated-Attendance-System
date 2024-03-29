import pyttsx3

class AudioEngine:
    #Setting up the module
    def __init__(self, id):    
        self.engine = pyttsx3.init('sapi5')
        self.id = id
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[id].id)

    #Converting from text to speech
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()