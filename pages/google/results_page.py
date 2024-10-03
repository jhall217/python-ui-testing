from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage
from pages.base.base_result import BaseResult


class GoogleResultsPage(BasePage, BaseResult):

    def __init__(self, browser):
        super().__init__(browser)
        self.result = BaseResult(browser)

    def __getattr__(self, name):
        return getattr(self.result, name)

    def results_count(self, phrase: str) -> int:
        xpath = f"//*[@id='search']/div/div/div//*[contains(text(),'{phrase}')]"
        elements = self.browser.find_elements(By.XPATH, xpath)
        return len(elements)
