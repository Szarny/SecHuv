import time
import base64
import os 
from typing import Tuple
import requests
from selenium import webdriver

FILENAME: str = "/project/util/tmp/tmp.jpg"

def take_screenshot(url: str) -> Tuple[bool, str]:
    try:
        _ = requests.get(url)

        driver: webdriver.PhantomJS = webdriver.PhantomJS("/project/util/selenium/phantomjs")
        driver.set_window_size(1920, 1080)
        driver.get(url)

        time.sleep(1)

        driver.save_screenshot(FILENAME)

        with open(FILENAME, "rb") as f:
            screenshot: str = base64.b64encode(f.read()).decode()

        return (True, screenshot)
    except:
        return (False, "")