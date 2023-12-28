import platform
from notifypy import Notify
notification = Notify(default_notification_title="Stock Notifier")

def os_notify(message):
    notification.message = message
    notification.send(block=False)