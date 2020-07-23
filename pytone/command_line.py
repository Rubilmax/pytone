import os
import sys
import time
import threading

from playsound import playsound

from .paths import get_random_soundfile, get_soundfile
from .notifications import notify


def run_python_command():
    if os.system("python " + " ".join(sys.argv[1:])):
        notify(message="An error occurred during your program execution!", duration=5.)
    else:
        notify()
        playsound(get_soundfile("nyancat"))
        time.sleep(.05)
