import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

IMPLICIT_WAIT_TIME = 10


def create_chrome_options():
    options = ChromeOptions()
    options.headless = True
    options.add_argument("--headless=new")
    return options


def create_webdriver(options):
    driver = webdriver.Chrome(options=options)  # Use the correct webdriver.Chrome
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)
    return driver


@pytest.fixture(autouse=True)
def browser():
    options = create_chrome_options()
    driver = create_webdriver(options)
    yield driver
    driver.quit()
