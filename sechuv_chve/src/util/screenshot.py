import time
import base64
import os 
from typing import Tuple
from selenium import webdriver

FILENAME: str = "/project/util/tmp/tmp.jpg"

def take_screenshot(url: str) -> Tuple[bool, str]:
    driver: webdriver.PhantomJS = webdriver.PhantomJS("/project/util/selenium/phantomjs")
    driver.set_window_size(1920, 1080)
    driver.get(url)

    time.sleep(0.5)

    driver.save_screenshot(FILENAME)

    with open(FILENAME, "rb") as f:
        screenshot: str = base64.b64encode(f.read()).decode()

    os.remove(FILENAME)

    return True, screenshot