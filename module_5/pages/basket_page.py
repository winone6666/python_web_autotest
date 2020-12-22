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

    def delete_item_from_basket(self):
        self.browser.find_element(*BasketPageLocators.DELETE_PRODUCT_BTN).click()

    def should_be_discount_input_form(self):
        assert self.is_element_present(*BasketPageLocators.DISCOUNT_CODE_INPUT), \
            'No field to fill in discount code'

    def apply_discount(self, discount_code):
        self.browser.find_element(*BasketPageLocators.BASKET_VOUCHER_INFO).click()
        self.should_be_discount_input_form()
        self.browser.find_element(*BasketPageLocators.DISCOUNT_CODE_INPUT).send_keys(discount_code)
        self.browser.find_element(*BasketPageLocators.APPLY_DISCOUNT_BTN).click()

    def should_be_success_applying_discount(self):
        self.apply_discount(self)
        assert self.is_element_present(*BasketPageLocators.DISCOUNT_SUCCESS_MESSAGE), \
            'The discount is not applied'
