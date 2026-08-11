import subprocess
import os
import datetime
import webbrowser

class ActionExecutor:
    def __init__(self):
        pass
    
    def execute(self, command_dict):
        action = command_dict.get("action")
        
        if action == "launch":
            return self.launch_app(command_dict)
        elif action == "system_info":
            return self.get_system_info(command_dict)
        elif action == "web_search":
            return self.web_search(command_dict)
        elif action == "system_command":
            return self.run_system_command(command_dict)
        
        return "Command not recognized"
    
    def launch_app(self, cmd):
        target = cmd.get("target")
        user = os.getenv("USERNAME")
        target = target.replace("{USER}", user)
        
        try:
            subprocess.Popen(target)
            return cmd.get("response", "Done")
        except Exception as e:
            return f"Failed to launch: {str(e)}"
    
    def get_system_info(self, cmd):
        info_type = cmd.get("info_type")
        
        if info_type == "time":
            now = datetime.datetime.now()
            return f"The time is {now.strftime('%I:%M %p')}"
        elif info_type == "date":
            today = datetime.datetime.now()
            return f"Today is {today.strftime('%A, %B %d, %Y')}"
        
        return "Information not available"
    
    def web_search(self, cmd):
        query = cmd.get("query", "")
        if not query:
            return "No search query provided"
        
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        
        try:
            webbrowser.open(search_url)
            return f"Searching Google for {query}"
        except Exception as e:
            return f"Failed to search: {str(e)}"
    
    def run_system_command(self, cmd):
        command = cmd.get("command")
        
        try:
            subprocess.Popen(command)
            return cmd.get("response", "Done")
        except Exception as e:
            return f"Failed to run command: {str(e)}"