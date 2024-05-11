
import os
import pygame
from openai import OpenAI
import os
import dotenv


dotenv.load_dotenv()



def generate_mp3(text):
    """
    This function gets the input as a string and saves the audio file.
    """
    client = OpenAI(
        base_url="https://api.avalai.ir/v1", api_key=os.environ.get("OPENAI_KEY")
    )
    try:
        with client.audio.speech.with_streaming_response.create(
            model="tts-1", voice="shimmer", input=text, speed=1.1
        ) as response:
            response.stream_to_file("speech.mp3")
            
    except Exception as e:
        print(e)

def play_mp3(file_path):
    """Function to play .mp3 file"""
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


if __name__ == "__main__":
    pass
