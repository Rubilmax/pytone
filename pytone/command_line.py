import os
import sys
import time
import threading
import pync

from playsound import playsound

from .paths import get_soundfile
from .notifications import notify


def run_python_command():
    os.system("python " + " ".join(sys.argv[1:]))
    soundfile = get_soundfile("nyancat")

    pync.notify('Hello World')
    print('test')
    pync.notify('Hello World', title='Python')

    pync.remove_notifications(os.getpid())

    pync.list_notifications(os.getpid())

    threading.Thread(target=notify).start()
    playsound(soundfile)

    time.sleep(1)
