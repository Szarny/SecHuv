import requests
from selenium import webdriver

from typing import Tuple


def get_html(url: str) -> Tuple[bool, str, str]:
    try:
        _ = requests.get(url)
        
        driver: webdriver.PhantomJS = webdriver.PhantomJS("/project/util/selenium/phantomjs")
        driver.get(url)

        body = driver.execute_script("return document.body.outerHTML;")
        raw_body = driver.execute_script("return document.body.innerText;")
        
        return (True, body, raw_body)
    except:
        return (False, "", "")