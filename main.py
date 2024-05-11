import pyperclip
from pathlib import Path
from openai import OpenAI
from utils import generate_audio

def main():
    """Main function to monitor clipboard and read new content"""
    # Initialize variable to store the last clipboard content
    last_clipboard_content = pyperclip.paste()

    while True:
        # Get the current clipboard content
        current_clipboard_content = pyperclip.paste()

        # Check if there is new content in the clipboard
        if current_clipboard_content != last_clipboard_content:
            print("New clipboard content detected:")
            print(current_clipboard_content)

            # Generate .mp3 file from the clipboard content
            generate_audio.generate_mp3(current_clipboard_content)
            print(current_clipboard_content)
            # Play the generated .mp3 file
            generate_audio.play_mp3('speech.mp3')  # Replace 'output.mp3' with the actual file path

            # Update the last clipboard content
            last_clipboard_content = current_clipboard_content

if __name__ == '__main__' : 
    main()