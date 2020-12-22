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

    def should_be_catalog_page(self):
        self.should_be_catalogue_url()
        self.should_be_short_product_info()

    def find_product(self, product_for_search):
        self.browser.find_element(*BasePageLocators.SEARCH_INPUT).send_keys(str(product_for_search))
        self.browser.find_element(*BasePageLocators.SEARCH_BTN).click()
        return self.browser.find_element(*ProductCatalogPageLocators.PRODUCT_NAME_IN_CATALOG).text

    def should_be_find_special_product(self, product_for_search):
        assert product_for_search == self.find_product(product_for_search), \
            'Found products is not equal of serched'
        assert self.is_element_present(*ProductCatalogPageLocators.HEADER_OF_PRODUCT_SEARCH_RU), \
            'No info about search result'

    def should_be_not_found_product_info(self, incorrect_text):
        self.browser.find_element(*BasePageLocators.SEARCH_INPUT).send_keys(str(incorrect_text))
        self.browser.find_element(*BasePageLocators.SEARCH_BTN).click()
        assert self.is_element_present(*ProductCatalogPageLocators.NO_PRODUCT_MESSAGE_RU), \
            'No info about not found product'

    def select_product(self):
        self.browser.find_element(*ProductCatalogPageLocators.ADD_TO_BASKET_BTN_IN_CATALOG).click()
