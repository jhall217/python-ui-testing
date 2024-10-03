from selenium.webdriver import Keys

from pages.base.base_search import BaseSearch
from pages.duckduckgo.results_page import DuckDuckGoResultsPage


class DuckDuckGoSearchPage(BaseSearch):
    URL = 'https://duckduckgo.com/'

    def search(self, input_text: str) -> DuckDuckGoResultsPage:
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(input_text + Keys.RETURN)
        return DuckDuckGoResultsPage(self.browser)


