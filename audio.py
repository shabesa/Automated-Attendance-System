class AudioEngine:
    #Setting up the module
    def __init__(self, engine, id):    
        self.engine = engine
        self.id = id
        self.voices = engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[id].id)

    #Converting from text to speech
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()