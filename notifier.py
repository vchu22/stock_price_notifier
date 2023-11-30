import platform
os_type = platform.system()

def os_notify(message):
    if os_type == 'Darwin':
        print(message)
        from pync import Notifier
        Notifier.notify(message, sound=True)
        