import os
import re
from pathlib import Path

import allure
import pytest
from playwright.sync_api import Page

from clients.user_client import UserClient
from config import VALID_USERNAME, VALID_PASSWORD
from pages.cart_page import CartPage

from pages.login_page import LoginPage
from pages.main_page import MainPage

SCREENSHOT_NAME_PATTERN = re.compile(r"^test-failed-\d+\.png$")
VIDEO_PATTERN = re.compile(r".*\.(webm|mp4)$")

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        for value in item.funcargs.values():
            if isinstance(value, Page):
                page = value
                break
        else:
            return

        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
        file_path = f"{screenshots_dir}/{item.name}.png"

        page.screenshot(path=file_path)
        allure.attach.file(
            file_path,
            name=item.name,
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.fixture(scope="function")
def login(page, request):
    username, password = request.param
    login_page = LoginPage(page)
    with allure.step("Open login page"):
        login_page.open()
        login_page.check_page()
    with allure.step("Enter valid username and password"):
        login_page.login(username, password)
    yield page


@pytest.fixture(scope="session")
def auth_state(browser):
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.open()
    login_page.check_page()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    context.storage_state(path="auth.json")

    context.close()


@pytest.fixture(scope="function")
def logged_user(auth_state, browser):
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()

    yield page

    context.close()


@pytest.fixture(scope="function")
def user_with_item_in_cart(logged_user):
    main_page = MainPage(logged_user)
    cart_page = CartPage(logged_user)

    main_page.open()
    main_page.check_page()
    main_page.page.wait_for_timeout(3000)

    item = main_page.add_first_item_to_cart()
    item_name = item.inner_text()
    main_page.page.wait_for_timeout(3000)

    cart_page.open()
    cart_page.check_page()
    main_page.page.wait_for_timeout(3000)

    cart_page.check_current_item_in_cart(item_name=item_name)
    cart_page.return_to_main_page()
    main_page.page.wait_for_timeout(3000)

    yield {
        "page": logged_user,
        "item_name": item_name
    }


@pytest.fixture
def user_client():
    return UserClient(base_url=BASE_URL)
