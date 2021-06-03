class AudioEngine:
    def __init__(self, engine, id):    
        self.engine = engine
        self.id = id
        self.voices = engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[id].id)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()