import allure
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Valid Login")
@allure.title("User can login")
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "login", [
        ("standard_user", "secret_sauce")
    ],
    indirect=True
)
def test_valid_user_login(login):
    main_page = MainPage(login)
    main_page.check_page()


@allure.feature("Invalid Login")
@allure.title("User can't login")
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "username, password, message", [
        ("invalid", "invalid", "Epic sadface: Username and password do not match any user in this service"),
        ("", "invalid", "Epic sadface: Username is required"),
        ("invalid", "", "Epic sadface: Password is required"),
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),

    ]
)
def test_invalid_user_login(page, username: str, password: str, message: str):
    allure.dynamic.feature("Invalid login cases")
    allure.dynamic.title(f"Check error message: {message}")
    allure.dynamic.story(f"{username} can't login")

    login_page = LoginPage(page)
    login_page.open()
    login_page.check_page()
    login_page.login(username, password)
    login_page.check_error_message(message)
