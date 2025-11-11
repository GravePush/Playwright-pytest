import allure
from playwright.sync_api import expect

from locators.checkout_locators import CheckoutCompleteLocators
from locators.components.header_locators import HeaderLocators
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    url = "https://www.saucedemo.com/checkout-complete.html"
    page_name = "Checkout Complete Page"

    def check_page(self):
        super().check_page()
        self.check_second_header_title_on_page(
            text="Checkout: Complete!",
            locator=HeaderLocators.SECOND_HEADER_TITLE
        )

    def check_complete_text(self):
        with allure.step("Check correct text"):
            expect(self.page.locator(CheckoutCompleteLocators.COMPLETE_TEXT)).to_have_text("Thank you for your order!")

    def back_to_home(self):
        with allure.step("Back to home"):
            self.page.locator(CheckoutCompleteLocators.BACK_TO_HOME_BUTTON).click()
