from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_url(self):
        login_url = self.browser.current_url
        assert "basket" in login_url, 'No word "basket" in current url'

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_RU_TEXT), \
            'No empty basket text'

    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOOD_ITEM), \
            "There is some items in basket"

    def should_not_be_checkout_btn_in_busket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CHECKOUT_BTN), \
            "There is checkout button on the page"

    def should_not_be_basket_total_info(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_VOUCHER_INFO), \
            "There is voucher to get discount in the basket"