import allure
from playwright.sync_api import Page, expect


class BasePage:
    url = None
    page_name = None

    def __init__(self, page: Page):
        self.page = page


    def open(self):
        with allure.step(f"Open {self.page_name} page"):
            self.page.goto(self.url)

    def check_title(self):
        expect(self.page).to_have_title("Swag Labs")

    def check_second_header_title_on_page(self, text: str, locator: str):
        expect(self.page.locator(locator)).to_have_text(text)

    def opened_page_have_url(self):
        self.page.wait_for_url(self.url)

    def opened_page_not_have_url(self):
        expect(self.page).not_to_have_url(self.url)

    def check_page(self):
        with allure.step(f"Check elements on {self.page_name} page"):
            self.check_title()
            self.opened_page_have_url()
