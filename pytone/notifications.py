import sys

from .paths import python_icon

if sys.platform != "darwin":
    def notify(message: str = "Your program has completed", duration: float = 10.):
        from pynotifier import Notification

        Notification(
            title="Python notification",
            description=message,
            icon_path=python_icon,
            duration=duration,
            urgency=Notification.URGENCY_CRITICAL
        ).send()
else:
    pass
