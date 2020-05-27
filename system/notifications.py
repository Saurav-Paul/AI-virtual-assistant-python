from plyer import notification

def notify(title='',msg='',t='5'):
    """Just give {title} {msg} {t} it will give the notification
        written by Saurav Paul """
    try :
        notification.notify(
            title = title,
            message = msg,
            timeout = t,
        )
    except Exception as e:
        pass
if __name__ == "__main__":
    notify('NotiFiCaTioN','Hi how are you',t=5)