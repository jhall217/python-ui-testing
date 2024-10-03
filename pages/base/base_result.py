from selenium.webdriver.common.by import By


class BaseResult:
    SEARCH_INPUT = (By.NAME, 'q')

    def __init__(self, browser):
        self.browser = browser

    def search_phrase(self) -> str:
        element = self.browser.find_element(*self.SEARCH_INPUT)
        return element.get_attribute('value')
