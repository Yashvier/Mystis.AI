COMMANDS = {
    "open chrome": {
        "action": "launch",
        "target": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "response": "Opening Chrome"
    },
    "open notepad": {
        "action": "launch",
        "target": "notepad.exe",
        "response": "Opening Notepad"
    },
    "what time is it": {
        "action": "system_info",
        "info_type": "time",
        "response": None
    },
    "what is today": {
        "action": "system_info",
        "info_type": "date",
        "response": None
    },
    "open file explorer": {
        "action": "launch",
        "target": "explorer.exe",
        "response": "Opening File Explorer"
    },
    "open vs code": {
        "action": "launch",
        "target": "C:\\Users\\{USER}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
        "response": "Opening Visual Studio Code"
    },
    "search google for": {
        "action": "web_search",
        "query_mode": True,
        "response": "Searching"
    },
    "lock screen": {
        "action": "system_command",
        "command": "rundll32.exe user32.dll,LockWorkStation",
        "response": "Locking screen"
    },
    "open settings": {
        "action": "launch",
        "target": "ms-settings:",
        "response": "Opening Settings"
    },
    "open documents": {
        "action": "launch",
        "target": "C:\\Users\\{USER}\\Documents",
        "response": "Opening Documents"
    }
}

def get_command(text):
    text_lower = text.lower().strip()
    
    for cmd_phrase, cmd_data in COMMANDS.items():
        if cmd_phrase in text_lower:
            result = dict(cmd_data)
            
            if cmd_data.get("query_mode"):
                query = text_lower.replace(cmd_phrase, "").strip()
                result["query"] = query if query else "general search"
            
            return result
    
    return None