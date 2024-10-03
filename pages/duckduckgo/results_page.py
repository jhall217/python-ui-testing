from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class DuckDuckGoResultsPage(BasePage):
    SEARCH_INPUT = (By.NAME, 'q')

    def results_count(self, SEARCH_PHRASE=None) -> int:
        xpath = f"//*[@id='react-layout']//li//*[contains(text(),'{SEARCH_PHRASE}')]"
        elements = self.browser.find_elements(By.XPATH, xpath)
        return len(elements)

    def search_phrase(self) -> str:
        element = self.browser.find_element(*self.SEARCH_INPUT)
        return element.get_attribute('value')
