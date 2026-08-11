import pyttsx3

class TTSEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
    
    def speak(self, text):
        print(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()