Clipboard Text-to-Speech Converter
================================

This project is a Python script that monitors the system clipboard and converts any new text content into an audio file using the OpenAI(AVAL AI) API. The generated audio file is then played back to the user.

Requirements
------------

* Python 3.11
* install with `pip install -r requirements.txt`)


Usage
-----

1. Install the required libraries
2. Run the script by executing `python main.py`
3. The script will start monitoring the system clipboard
4. When new text content is detected in the clipboard, the script will generate an audio file and play it back to the user

Note
----

* This script uses the OpenAI(AVAL AI) API to generate the audio file. You may need to obtain an API key from OpenAI(AVAL AI) and configure it in the script.
* The script generates an audio file named `speech.mp3` in the current working directory. You may want to modify the script to use a different file name or location.
