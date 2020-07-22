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
        import pync 
        pync.notify(message, title=title)
        pync.remove_notifications(os.getpid())

        pync.list_notifications(os.getpid())
