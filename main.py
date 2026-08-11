from stt import STTEngine
from parser import CommandParser
from executor import ActionExecutor
from tts import TTSEngine

# Initialize all engines
stt = STTEngine()
parser = CommandParser()
executor = ActionExecutor()
tts = TTSEngine()

# Main loop
while True:
    text = stt.listen()
    
    if text is None:
        continue
    
    command = parser.parse(text)
    
    if command is None:
        tts.speak("I did not understand that")
        continue
    
    response = executor.execute(command)
    tts.speak(response)