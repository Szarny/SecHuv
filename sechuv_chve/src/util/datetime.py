import datetime

def get_current() -> str:
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")