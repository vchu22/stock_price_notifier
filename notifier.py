import platform
from notifypy import Notify
import os

icon = os.path.join(os.getcwd(), "stock-96.png")
audio = os.path.join(os.getcwd(), "notification.wav")
notification = Notify(default_notification_title="Stock Price Notifier",
                      default_application_name="Stock Price Notifier", default_notification_icon=icon,
                      default_notification_audio=audio)


def os_notify(message):
    notification.message = message
    notification.send(block=False)
