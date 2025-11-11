import allure
from playwright.sync_api import expect

from locators.cart_page_locators import CartPageLocators
from locators.components.header_locators import HeaderLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    url = "https://www.saucedemo.com/cart.html"
    page_name = "Cart"

    def check_page(self):
        super().check_page()
        self.check_second_header_title_on_page(text="Your Cart", locator=HeaderLocators.SECOND_HEADER_TITLE)

    def return_to_main_page(self):
        with allure.step("Return to main page"):
            locator = self.page.locator(CartPageLocators.BACK_TO_MAIN_PAGE)
            expect(locator).to_be_visible()
            locator.click()

    def check_current_item_in_cart(self, item_name: str):
        with allure.step("Check current item in cart"):
            expect(self.page.get_by_role("link", name=item_name)).to_be_visible()

    def check_current_item_not_in_cart(self, item_name: str):
        with allure.step("Check current item not in cart"):
            expect(self.page.get_by_role("link", name=item_name)).not_to_be_visible()

    def click_checkout_items(self):
        with allure.step("Click checkout button"):
            self.page.locator(CartPageLocators.CHECKOUT_BUTTON).click()

    def remove_item_from_cart_page(self, item_name: str):
        with allure.step("Remove item from cart"):
            expect(self.page.locator(CartPageLocators.ITEM_NAME)).to_have_text(item_name)
            self.page.get_by_role("button", name=CartPageLocators.REMOVE_BUTTON).click()
            expect(self.page.locator(HeaderLocators.CART_BADGE)).not_to_be_visible()
