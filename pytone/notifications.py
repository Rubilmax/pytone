from plyer import notification

from .paths import python_icon


def notify(title: str = "Python notification", message: str = "Your program has completed"):
    notification.notify(
        title=title,
        message=message,
        app_name="Python",
        app_icon=python_icon
    )
