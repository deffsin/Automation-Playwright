from playwright.sync_api import Page

class BasePage:
    url: str | None = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.url:
            self.page.goto(self.url)
        else:
            raise ValueError("Not possible to open page without URL")