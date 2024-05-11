import pyperclip
from utils import generate_audio


def main():
    last_clipboard_content = pyperclip.paste()
    while True:

        current_clipboard_content = pyperclip.paste()

        if current_clipboard_content != last_clipboard_content:
            print("New clipboard content detected:")
            print(current_clipboard_content)
            
            generate_audio.generate_mp3(current_clipboard_content)
            generate_audio.play_mp3("speech.mp3")
            last_clipboard_content = current_clipboard_content


if __name__ == "__main__":
    main()
