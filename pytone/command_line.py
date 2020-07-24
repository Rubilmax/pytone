import os
import sys
import time
import argparse

from .notifications import notify


def run_python_command():
    nb_args = len(sys.argv)
    file_pos = next((i for i in range(1, nb_args) if sys.argv[i].endswith(".py")), nb_args)
    python_command = "python " + " ".join(sys.argv[file_pos:])
    pytone_args = filter(lambda arg: arg.startswith("--"), sys.argv[1:file_pos])

    parser = argparse.ArgumentParser(description="Pytone arguments")
    parser.add_argument("--mute", action="store_true")
    parser.add_argument("--sound", default="random", nargs=1, type=str)
    namespace = parser.parse_args(pytone_args)

    if os.system(python_command):
        notify(message="An error occurred during your program execution!", duration=5.)
    else:
        sound = namespace.sound if not namespace.mute else None
        notify(sound=sound)
        time.sleep(.05)
