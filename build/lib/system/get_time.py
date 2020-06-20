
from datetime import datetime
import time

def get_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
def digital_time():
    return time.strftime("%B %d, %Y %-I:%M %p")

if __name__ == "__main__":
    print(get_time())
    print(digital_time())