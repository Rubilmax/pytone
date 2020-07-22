import os
import sys
import glob
import random

file_dir = os.path.dirname(os.path.abspath(__file__))

if sys.platform == "win32":
    python_icon = os.path.join(file_dir, "assets", "python.ico")
elif sys.platform == "linux":
    python_icon = os.path.join(file_dir, "assets", "python.png")
elif sys.platform == "darwin":
    python_icon = None


def get_soundfile(sound_name: str):
    return os.path.join(file_dir, "assets", "sounds", f"{sound_name}.mp3")


def get_random_soundfile():
    filenames = glob.glob(os.path.join(file_dir, "assets", "sounds", "*.mp3"))
    return random.choice(filenames)
