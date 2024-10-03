from selenium.webdriver import Keys

from pages.base.base_search import BaseSearch
from pages.google.results_page import GoogleResultsPage


class GoogleSearchPage(BaseSearch):
    URL = 'https://google.com/'

    def search(self, input_text: str) -> GoogleResultsPage:
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(input_text + Keys.RETURN)
        return GoogleResultsPage(self.browser)
