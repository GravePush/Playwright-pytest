import allure

from pages.cart_page import CartPage
from pages.main_page import MainPage


@allure.feature("Remove item from cart")
@allure.title("Logged user with item in cart can remove this item from cart")
@allure.severity(severity_level=allure.severity_level.CRITICAL)
def test_remove_item_from_cart(user_with_item_in_cart):
    page = user_with_item_in_cart["page"]
    item_name = user_with_item_in_cart["item_name"]
    cart_page = CartPage(page)
    main_page = MainPage(page)
    main_page.click_on_cart()
    cart_page.remove_item_from_cart_page(item_name=item_name)

    cart_page.check_current_item_not_in_cart(item_name=item_name)
    cart_page.page.wait_for_timeout(3000)
