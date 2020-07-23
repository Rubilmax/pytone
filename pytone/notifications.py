import sys
import os

from .paths import python_icon


def notify(
        title='Python notification',
        message: str = "Your program has completed",
        duration: float = 10.
    ):
    if sys.platform != "darwin":
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
