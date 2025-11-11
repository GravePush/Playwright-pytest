class CheckoutStepOneLocators:
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"


class CheckoutStepTwoLocators:
    ITEM_PRICE_BY_NAME = (
        ".cart_item:has(.inventory_item_name:text('{item_name}')) "
        ".inventory_item_price"
    )
    TAX = "[data-test='tax-label']"
    TOTAL_PRICE = "[data-test='total-label']"
    FINISH_BUTTON = "#finish"


class CheckoutCompleteLocators:
    COMPLETE_TEXT = "[data-test='complete-header']"
    BACK_TO_HOME_BUTTON = "#back-to-products"
