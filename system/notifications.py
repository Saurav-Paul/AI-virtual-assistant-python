from plyer import notification

def notify(title='',msg='',t='5'):
    try :
        notification.notify(
            title = title,
            message = msg,
            timeout = t,
        )
    except Exception as e:
        pass
if __name__ == "__main__":
    notify('NotiFiCaTioN','Love you',t=5)