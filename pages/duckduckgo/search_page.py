from selenium.webdriver import Keys

from pages.base.base_search import BaseSearch
from pages.duckduckgo.results_page import DuckDuckGoResultsPage


class DuckDuckGoSearchPage(BaseSearch):
    URL = 'https://duckduckgo.com/'

    def search(self, input_text: str) -> DuckDuckGoResultsPage:
        super().search(input_text)
        return DuckDuckGoResultsPage(self.browser)
