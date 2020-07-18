from playsound import playsound
import time
import sys
import os

file_dir = os.path.dirname(os.path.abspath(__file__))


def run_python_command():
    os.system("python " + " ".join(sys.argv[1:]))
    soundfile = os.path.join(file_dir, "assets", "nyancat.mp3")
    playsound(soundfile)
    time.sleep(1)
