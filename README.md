#Mystis.AI

A Jarvis-inspired voice-controlled desktop AI assistant for Windows. Mystis.AI responds to natural voice commands and executes actions across your system, powered by modular Python architecture.

Features

Voice Control: Listen for voice commands and respond with text-to-speech feedback
Command Parsing: Understand natural language input and execute system actions
Extensible Architecture: Modular design allows easy addition of new capabilities
Windows Integration: Automate applications, open files, control system functions
Intelligent Responses: AI-driven assistant that maintains context and personality

System Requirements

Windows 10 or later
Python 3.8 or higher
Microphone for voice input
Speaker or headphones for audio output

Installation

Clone the repository:

git clone https://github.com/Yashvier/Mystis.AI.git
cd Mystis.AI

Install dependencies:

pip install -r requirements.txt

Configure your API key:

Create a config file in the project root with your Anthropic API credentials

Run the assistant:

python main.py

Architecture

Mystis.AI uses a modular design with six core components:

STTEngine (stt.py): Speech-to-text conversion using Google Speech Recognition
CommandParser (parser.py): Parses voice input into executable commands
ActionExecutor (executor.py): Executes system commands and actions
TTSEngine (tts.py): Text-to-speech responses using pyttsx3
CommandRegistry (commands.py): Manages available voice commands
Main Controller (main.py): Orchestrates all components

Dependencies

SpeechRecognition: Voice input processing
pyttsx3: Text-to-speech synthesis
PyAutoGUI: System automation and control
Anthropic API: AI-powered language understanding

For detailed dependencies, see requirements.txt

Usage

Start the assistant:

python main.py

The assistant listens for voice commands. Examples of supported commands:

"Open notepad"
"What time is it"
"Search for Python documentation"
"Take a screenshot"
"Tell me a joke"

The assistant will process your command and respond with voice feedback confirming the action.

Project Structure

main.py: Entry point and main event loop
stt.py: Speech recognition engine
parser.py: Command parsing and interpretation
executor.py: Command execution logic
tts.py: Text-to-speech engine
commands.py: Available command definitions
commands.txt: Command configuration file

Configuration

Customize available commands by editing commands.txt or adding new command handlers to commands.py. The assistant uses a system prompt to maintain its identity. Configure this in the main configuration file.

Development

The modular architecture makes it simple to extend functionality:

Add new commands to CommandRegistry
Create new command handlers in executor.py
Integrate additional APIs or services through the ActionExecutor

Known Limitations

Requires Windows operating system
Voice recognition accuracy depends on microphone quality and ambient noise
Some advanced system actions require administrator privileges

Troubleshooting

Assistant stops responding after unrecognized command: Ensure speech recognition service is running and restart the application
API connection errors: Verify your Anthropic API key and internet connection
Audio issues: Check microphone permissions and speaker configuration in Windows settings

License

This project is under development. See LICENSE for details.

Contributing

Contributions are welcome. Fork the repository and submit pull requests with improvements or new features.

Contact

For questions or feedback, open an issue on the GitHub repository.

Status

In Development (InDEV). Core features are functional. API integration and advanced automation features are ongoing.
