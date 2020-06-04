
from datetime import datetime
import time

def get_time():
    return datetime.now().strftime('%H:%M:%S %d-%m-%Y')

def digital_time():
    return time.strftime("%b %d %Y %-I:%M %p")

if __name__ == "__main__":
    print(digital_time())