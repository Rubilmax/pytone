from playsound import playsound
import time
import sys
import os


def run_python_command():
    os.system("python " + " ".join(sys.argv[1:]))
    playsound("./pytone/assets/nyancat.mp3")
    time.sleep(1)
