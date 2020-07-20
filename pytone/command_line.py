import os
import sys
import time
import threading

from playsound import playsound

from .paths import get_soundfile
from .notifications import notify


def run_python_command():
    if os.system("python " + " ".join(sys.argv[1:])) != 0:
        notify("An error occurred during your program execution!", timeout=5.)
    else:
        soundfile = get_soundfile("nyancat")

        threading.Thread(target=notify).start()
        playsound(soundfile)
        time.sleep(.1)
