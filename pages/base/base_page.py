class BasePage:
    URL = ''

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def title(self) -> str:
        return self.browser.title
