from selenium.webdriver import Keys

from pages.base.base_search import BaseSearch
from pages.google.results_page import GoogleResultsPage


class GoogleSearchPage(BaseSearch):
    URL = 'https://google.com/'

    def search(self, input_text: str) -> GoogleResultsPage:
        super().search(input_text)
        return GoogleResultsPage(self.browser)
