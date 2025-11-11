import allure

from locators.checkout_locators import CheckoutStepOneLocators
from locators.components.header_locators import HeaderLocators
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    url = "https://www.saucedemo.com/checkout-step-one.html"
    page_name = "Checkout Page Step One"


    def check_page(self):
        super().check_page()
        self.check_second_header_title_on_page(
            text="Checkout: Your Information",
            locator=HeaderLocators.SECOND_HEADER_TITLE
        )

    def input_valid_data(self, first_name: str, last_name: str, postal_code: str):
        with allure.step("Input valid data"):
            self.page.locator(CheckoutStepOneLocators.FIRST_NAME).fill(first_name)
            self.page.locator(CheckoutStepOneLocators.LAST_NAME).fill(last_name)
            self.page.locator(CheckoutStepOneLocators.POSTAL_CODE).fill(postal_code)

    def click_on_continue_button(self):
        with allure.step("Click on continue button"):
            self.page.locator(CheckoutStepOneLocators.CONTINUE_BUTTON).click()
