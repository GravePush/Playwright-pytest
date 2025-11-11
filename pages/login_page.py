import allure
from playwright.sync_api import expect, Locator

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    url = "https://www.saucedemo.com/"
    page_name = "Login"

    def _login_steps(self, username: str, password: str):
        self.page.locator(LoginPageLocators.USERNAME).fill(username)
        self.page.locator(LoginPageLocators.PASSWORD).fill(password)
        self.page.locator(LoginPageLocators.LOGIN_BUTTON).click()

    def login(self, username: str, password: str):
        self._login_steps(username, password)

    def check_error_message(self, message):
        with allure.step("Check error message"):
            error_locator = self.page.locator(LoginPageLocators.ERROR_MESSAGE)
            expect(error_locator).to_have_text(message)


