import allure
import pytest

from config import FIRST_NAME_CHECKOUT, POSTAL_CODE_CHECKOUT, LAST_NAME_CHECKOUT
from pages.cart_page import CartPage
from pages.checkout_pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.main_page import MainPage


@allure.tag("e2e", "smoke")
@allure.feature("Purchase item")
@allure.title("User can purchase item")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.e2e
@pytest.mark.parametrize(
    "login", [
        ("standard_user", "secret_sauce")
    ],
    indirect=True
)
def test_user_can_purchase_item(login):
    page = login
    main_page = MainPage(page)
    main_page.open()
    main_page.check_page()

    item = main_page.add_first_item_to_cart()
    item_name = item.inner_text()

    main_page.click_on_cart()

    cart_page = CartPage(page)
    cart_page.check_page()

    cart_page.check_current_item_in_cart(item_name=item_name)

    cart_page.click_checkout_items()

    checkout_page_step_one = CheckoutStepOnePage(page)
    checkout_page_step_one.check_page()

    checkout_page_step_one.input_valid_data(
        FIRST_NAME_CHECKOUT,
        LAST_NAME_CHECKOUT,
        POSTAL_CODE_CHECKOUT
    )
    checkout_page_step_one.click_on_continue_button()

    checkout_page_step_two = CheckoutStepTwoPage(page)
    checkout_page_step_two.check_page()

    checkout_page_step_two.check_final_price_with_tax(item_name=item_name)
    checkout_page_step_two.click_on_finish_button()

    checkout_page_complete = CheckoutCompletePage(page)
    checkout_page_complete.check_page()

    checkout_page_complete.check_complete_text()

    checkout_page_complete.back_to_home()
    main_page.check_page()
