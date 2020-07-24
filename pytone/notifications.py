import sys
import os

from playsound import playsound

from .paths import python_icon, get_random_soundfile, get_soundfile


def notify(
    title="Python notification",
    message: str = "Your program has completed",
    duration: float = 10.,
    sound: str = None
):
    if sys.platform != "darwin":
        # pynotifier is windows+linux
        from pynotifier import Notification

        Notification(
            title=title,
            description=message,
            icon_path=python_icon,
            duration=duration,
            urgency=Notification.URGENCY_CRITICAL
        ).send()
    else:
        from pync import Notifier

        Notifier.notify(message, title=title)
        Notifier.remove(os.getpid())
        Notifier.list(os.getpid())

    if sound is not None:
        if sound == "random":
            soundfile = get_random_soundfile()
        else:
            soundfile = get_soundfile(sound)

        playsound(soundfile)
