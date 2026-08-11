import speech_recognition as sr

class STTEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
    
    def listen(self, timeout=10):
        try:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=timeout)
            
            text = self.recognizer.recognize_google(audio)
            print(f"Heard: {text}")
            return text
        
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Error contacting Google API: {e}")
            return None
        except sr.WaitTimeoutError:
            print("No speech detected")
            return None
        