import re
from pathlib import Path

import allure
import pytest

from config import VALID_USERNAME, VALID_PASSWORD
from pages.cart_page import CartPage

from pages.login_page import LoginPage
from pages.main_page import MainPage

SCREENSHOT_NAME_PATTERN = re.compile(r"^test-failed-\d+\.png$")
VIDEO_PATTERN = re.compile(r".*\.(webm|mp4)$")


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_teardown(item, nextitem):
#     yield
#
#     try:
#         artifacts_dir = item.funcargs.get("allure-results")
#         if artifacts_dir:
#             artifacts_dir_path = Path(artifacts_dir)
#             if artifacts_dir_path.is_dir():
#                 for file in artifacts_dir_path.iterdir():
#                     if file.is_file() and SCREENSHOT_NAME_PATTERN.match(file.name):
#                         allure.attach.file(
#                             str(file),
#                             name=file.name,
#                             attachment_type=allure.attachment_type.PNG,
#                         )
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # выполняем тест
    outcome = yield
    report = outcome.get_result()
    try:
        if report.failed:
            screenshots_dir = Path("allure-results")
            if screenshots_dir.exists():
                for file in screenshots_dir.glob("*.png"):
                    if file.is_file() and SCREENSHOT_NAME_PATTERN.match(file.name):
                        allure.attach.file(
                            str(file),
                            name=file.name,
                            attachment_type=allure.attachment_type.PNG
                        )
                    elif VIDEO_PATTERN.match(file.name):
                        allure.attach.file(
                            str(file),
                            name="Video on failure",
                            attachment_type=allure.attachment_type.WEBM,
                        )

    except Exception as e:
        print(f"Error taking screenshot: {e}")


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



@pytest.fixture(scope="session", params=[(VALID_USERNAME, VALID_PASSWORD)])
def auth_state(browser, request):
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.open()
    login_page.check_page()
    login_page.login(*request.param)

    context.storage_state(path="auth.json")
    context.close()


@pytest.fixture(scope="function")
def logged_user(browser, auth_state):
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
    item = main_page.add_first_item_to_cart()
    item_name = item.inner_text()

    cart_page.open()
    cart_page.check_page()
    cart_page.check_current_item_in_cart(item_name=item_name)
    cart_page.return_to_main_page()

    yield {
        "page": logged_user,
        "item_name": item_name
    }
