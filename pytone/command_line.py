from playsound import playsound
import time
import sys
import os


def run_python_command():
    print(sys.argv)
    playsound("assets/nyancat.mp3")
    time.sleep(1)
