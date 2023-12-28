import platform
from pync import Notifier
os_type = platform.system()

def os_notify(message):
    if os_type == 'Darwin':
        print(message)
        Notifier.notify(message, sound=True)