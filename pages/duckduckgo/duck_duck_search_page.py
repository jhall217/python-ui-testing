from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base.base_search import BaseSearch
from pages.duckduckgo.duck_duck_results_page import DuckDuckGoResultsPage


class DuckDuckGoSearchPage(BaseSearch):
    URL = 'https://duckduckgo.com/'

    SEARCH_BUTTON = (By.XPATH, '//*[@id="searchbox_homepage"]//button')

    def search(self, input_text: str) -> DuckDuckGoResultsPage:
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(input_text + Keys.RETURN)
        return DuckDuckGoResultsPage(self.browser)


