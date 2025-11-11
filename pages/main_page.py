import allure
from playwright.sync_api import expect, Locator

from locators.components.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from .base_page import BasePage


@allure.feature("Main Page")
class MainPage(BasePage):
    url = "https://www.saucedemo.com/inventory.html"
    page_name = "Main"

    def check_page(self):
        super().check_page()
        self.check_second_header_title_on_page(text="Products", locator=HeaderLocators.SECOND_HEADER_TITLE)

    def _get_first_item_on_page(self):
        first_item_on_page = self.page.locator(MainPageLocators.FIRST_ITEM_ON_PAGE).first
        expect(first_item_on_page).to_be_visible()
        return first_item_on_page

    def add_first_item_to_cart(self):
        with allure.step("Add first item to cart"):
            first_item = self._get_first_item_on_page()
            first_item.get_by_role("button", name=MainPageLocators.ADD_TO_CART).click()
            expect(self.page.locator(HeaderLocators.CART_BADGE)).to_be_visible()
            first_item_name = first_item.locator(MainPageLocators.ITEM_NAME)

        return first_item_name

    def remove_item_from_main_page(self):
        with allure.step("Remove item from main page"):
            item = self._get_first_item_on_page()
            item.get_by_role("button", name=MainPageLocators.REMOVE_BUTTON).click()
            expect(self.page.locator(HeaderLocators.CART_BADGE)).not_to_be_visible()

    def click_on_cart(self):
        with allure.step("Click on cart"):
            self.page.locator(HeaderLocators.CART_LINK).click()
