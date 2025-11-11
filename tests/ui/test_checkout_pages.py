import allure
import pytest

from config import FIRST_NAME_CHECKOUT, POSTAL_CODE_CHECKOUT, LAST_NAME_CHECKOUT
from pages.checkout_pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.main_page import MainPage


@allure.feature("Valid input in checkout step one")
@allure.title("Logged user with item in cart input valid data on page and continue checkout")
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "first_name, last_name, postal_code", [
        (FIRST_NAME_CHECKOUT, LAST_NAME_CHECKOUT, POSTAL_CODE_CHECKOUT)
    ]
)
def test_valid_input_on_checkout_step_one_page(
        user_with_item_in_cart,
        first_name,
        last_name,
        postal_code
):
    page = user_with_item_in_cart["page"]

    check_out_page_one = CheckoutStepOnePage(page)
    check_out_page_two = CheckoutStepTwoPage(page)

    check_out_page_one.open()
    check_out_page_one.check_page()
    check_out_page_one.input_valid_data(first_name, last_name, postal_code)
    check_out_page_one.click_on_continue_button()

    check_out_page_two.check_page()


@allure.feature("Check info on checkout step two")
@allure.title("Check correct info about added item and continue checkout")
@allure.severity(severity_level=allure.severity_level.NORMAL)
def test_check_correct_info_checkout_two_page(user_with_item_in_cart):
    page = user_with_item_in_cart["page"]
    item_name = user_with_item_in_cart["item_name"]

    check_out_page_one = CheckoutStepOnePage(page)
    check_out_page_one.open()
    check_out_page_one.check_page()
    check_out_page_one.input_valid_data(FIRST_NAME_CHECKOUT, LAST_NAME_CHECKOUT, POSTAL_CODE_CHECKOUT)
    check_out_page_one.click_on_continue_button()

    check_out_page_two = CheckoutStepTwoPage(page)
    check_out_page_two.check_page()
    check_out_page_two.check_final_price_with_tax(item_name=item_name)
    check_out_page_two.click_on_finish_button()

    check_out_page_complete = CheckoutCompletePage(page)
    check_out_page_complete.check_page()


@allure.feature("Complete checkout")
@allure.title("Check correct message about successful purchase and back to main menu")
@allure.severity(severity_level=allure.severity_level.MINOR)
def test_checkout_complete_page(user_with_item_in_cart):
    page = user_with_item_in_cart["page"]
    item_name = user_with_item_in_cart["item_name"]

    check_out_page_one = CheckoutStepOnePage(page)
    check_out_page_one.open()
    check_out_page_one.check_page()
    check_out_page_one.input_valid_data(FIRST_NAME_CHECKOUT, LAST_NAME_CHECKOUT, POSTAL_CODE_CHECKOUT)
    check_out_page_one.click_on_continue_button()

    check_out_page_two = CheckoutStepTwoPage(page)
    check_out_page_two.check_page()
    check_out_page_two.check_final_price_with_tax(item_name=item_name)
    check_out_page_two.click_on_finish_button()

    check_out_page_complete = CheckoutCompletePage(page)
    check_out_page_complete.check_page()
    check_out_page_complete.check_complete_text()
    check_out_page_complete.back_to_home()

    main_page = MainPage(page)
    main_page.check_page()
