from .base_page import BasePage
from .locators import ProductCatalogPageLocators
from .locators import BasePageLocators

class ProductCatalogPage(BasePage):
    def should_be_catalogue_url(self):
        login_url = self.browser.current_url
        assert "catalogue" in login_url, 'No word "catalogue" in current url'

    def should_be_short_product_info(self):
        assert self.is_element_present(*ProductCatalogPageLocators.PRODUCT_IMAGE_IN_CATALOG), \
            'No product image'
        assert self.is_element_present(*ProductCatalogPageLocators.PRODUCT_RATING_INFO_IN_CATALOG), \
            'No info about product rating'
        assert self.is_element_present(*ProductCatalogPageLocators.PRODUCT_NAME_IN_CATALOG), \
            'No info about product name'
        assert self.is_element_present(*ProductCatalogPageLocators.PRODUCT_AMOUNT_IN_CATALOG), \
            'No info about product amount'
        assert self.is_element_present(*ProductCatalogPageLocators.PRODUCT_STORE_INFO_IN_CATALOG), \
            'No info about storing product'

    def find_product(self, product_for_search):
        search_input = self.browser.find_element(*BasePageLocators.SEARCH_INPUT)
        search_input.send_keys(product_for_search)
        search_btn = self.browser.find_element(*BasePageLocators.SEARCH_BTN)
        search_btn.click()
        return product_for_search

    def should_be_find_special_product(self, name_of_found_product):
        assert name_of_found_product == self.find_product(self), \
        'Found products is not equal of serched'
        assert self.is_element_present(
            *ProductCatalogPageLocators.HEADER_OF_PRODUCT_SEARCH_RU + "\"{}\"".format(name_of_found_product)), \
            'No info about search result'

    def should_be_not_found_product_info(self):
        self.find_product(self)
        assert self.is_element_present(*ProductCatalogPageLocators.NO_PRODUCT_MESSAGE_RU), \
            'No info about not found product'