import allure
from playwright.sync_api import expect

from locators.checkout_locators import CheckoutStepTwoLocators
from locators.components.header_locators import HeaderLocators
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    url = "https://www.saucedemo.com/checkout-step-two.html"
    page_name = "Checkout Page Step Two"

    def check_page(self):
        super().check_page()
        self.check_second_header_title_on_page(
            text="Checkout: Overview",
            locator=HeaderLocators.SECOND_HEADER_TITLE
        )

    def check_final_price_with_tax(self, item_name: str):
        with allure.step("Сheck final price with tax"):
            item = self.page.get_by_role("link", name=item_name)
            expect(item).to_be_visible()

            item_price = self.page.locator(CheckoutStepTwoLocators.ITEM_PRICE_BY_NAME.format(item_name=item_name))
            item_price = float(item_price.inner_text().strip("$"))
            tax = self.page.locator(CheckoutStepTwoLocators.TAX)
            tax = tax.inner_text().replace("Tax: $", "")
            total_price_expected = float(item_price) + float(tax)

            total_price_locator = self.page.locator(
                CheckoutStepTwoLocators.TOTAL_PRICE
            )
            expect(total_price_locator).to_have_text(f"Total: ${total_price_expected}")

    def click_on_finish_button(self):
        with allure.step("Click on finish button"):
            self.page.locator(CheckoutStepTwoLocators.FINISH_BUTTON).click()
