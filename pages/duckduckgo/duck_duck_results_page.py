from selenium.webdriver.common.by import By

from pages.base.base_page import BasePage


class DuckDuckGoResultsPage(BasePage):
    URL = 'https://duckduckgo.com/'
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_PHRASE = 'cat'

    def results_count(self, SEARCH_PHRASE=None) -> int:
        xpath = f"//div[@id='links']//*[contains(text(), '{SEARCH_PHRASE}')]"
        elements = self.browser.find_elements(xpath)
        return len(elements)

    def search_phrase(self) -> str:
        element = self.browser.find_element(*self.SEARCH_INPUT)
        return element.get_attribute('value')
