from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def open_math_alert(self):
        self.should_be_promo_url()
        self.click_add_to_basket_btn()

    def should_be_promo_url(self):
        login_url = self.browser.current_url
        assert "?promo" in login_url, 'No word "?promo" in current url'

    def click_add_to_basket_btn(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_equal_amount_in_basket(self):
        book_price_on_page = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_PAGE).text
        info_amount_in_basket = self.browser.find_element(*ProductPageLocators.INFO_AMOUNT_OF_BASKET).text
        assert book_price_on_page == info_amount_in_basket, 'The basket\'s amount is not equal the book\'s price on page {} = '\
            .format(info_amount_in_basket)

    def should_be_equal_product_name_in_basket(self):
        book_name_on_page = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_PAGE).text
        info_book_name_in_basket = self.browser.find_element(*ProductPageLocators.INFO_BOOK_NAME_IN_BASKET).text
        assert book_name_on_page == info_book_name_in_basket, 'The book\'s name in basket is not equal this one on page {} = '\
            .format(info_book_name_in_basket)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_element_visible(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not visible, but it was visible before"
