from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base.base_page import BasePage


class BaseSearch(BasePage):
    SEARCH_INPUT = (By.NAME, 'q')

    def search(self, input_text: str):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(input_text + Keys.RETURN)
