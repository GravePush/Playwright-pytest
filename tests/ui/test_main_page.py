import allure
import pytest

from pages.cart_page import CartPage
from pages.main_page import MainPage


@allure.feature("Add item to cart")
@allure.title("Logged user can add item to cart")
@allure.severity(severity_level=allure.severity_level.CRITICAL)
def test_add_first_item_to_cart(logged_user):
    main_page = MainPage(logged_user)
    main_page.open()
    main_page.check_page()

    item = main_page.add_first_item_to_cart()
    item_name = item.inner_text()
    main_page.click_on_cart()

    cart_page = CartPage(logged_user)
    cart_page.check_page()
    cart_page.check_current_item_in_cart(item_name=item_name)


@allure.feature("Remove item to cart")
@allure.title("Logged user with item in cart can remove item from main page")
@allure.severity(severity_level=allure.severity_level.CRITICAL)
def test_remove_item_from_main_page(user_with_item_in_cart):
    page = user_with_item_in_cart["page"]
    item_name = user_with_item_in_cart["item_name"]

    main_page = MainPage(page)
    cart_page = CartPage(page)

    main_page.remove_item_from_main_page()

    cart_page.open()
    cart_page.check_page()
    cart_page.check_current_item_not_in_cart(item_name=item_name)
    cart_page.return_to_main_page()

    main_page.check_page()
