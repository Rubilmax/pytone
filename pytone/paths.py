import os
import sys
import glob
import random

file_dir = os.path.dirname(os.path.abspath(__file__))

icon_ext = "ico" if sys.platform == "win32" else "png"
python_icon = os.path.join(file_dir, "assets", f"python.{icon_ext}")


def get_soundfile(sound_name: str):
    return os.path.join(file_dir, "assets", "sounds", f"{sound_name}.mp3")


def get_random_soundfile():
    filenames = glob.glob(os.path.join(file_dir, "assets", "sounds", "*.mp3"))
    return random.choice(filenames)
