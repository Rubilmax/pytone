from plyer import notification

from .paths import python_icon


def notify(message: str = "Your program has completed", timeout: float = 10.):
    notification.notify(
        title="Python notification",
        message=message,
        app_name="Python",
        app_icon=python_icon,
        timeout=timeout
    )
