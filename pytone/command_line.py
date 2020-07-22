import os
import sys
import time

from playsound import playsound

from .paths import get_random_soundfile
from .notifications import notify


def run_python_command():
    if os.system("python " + " ".join(sys.argv[1:])):
        notify("An error occurred during your program execution!", duration=5.)
    else:
        soundfile = get_random_soundfile()

        notify()
        playsound(soundfile)
        time.sleep(.1)
