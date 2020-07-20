import os

file_dir = os.path.dirname(os.path.abspath(__file__))

python_icon = os.path.join(file_dir, "assets", "python.ico")


def get_soundfile(sound_name: str):
    return os.path.join(file_dir, "assets", "sounds", f"{sound_name}.mp3")
