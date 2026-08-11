from commands import get_command

class CommandParser:
    def __init__(self):
        pass
    
    def parse(self, text):
        if not text:
            return None
        
        command = get_command(text)
        return command