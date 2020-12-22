import pytest

from .pages.basket_page import BasketPage
from .pages.product_catalog_page import ProductCatalogPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"


class TestBasketPage:
    @pytest.mark.xfail(reason='TODO Fix DELETE product button')
    def test_user_can_delete_product_from_basket(self, browser):
        page = ProductCatalogPage(browser, link)
        page.open()
        page.select_product()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.delete_item_from_basket()
        basket_page.should_not_be_goods_in_basket()
        basket_page.should_not_be_basket_total_info()
        basket_page.should_not_be_checkout_btn_in_busket()

    def test_user_can_use_discount(self, browser):
        page = ProductCatalogPage(browser, link)
        page.open()
        page.select_product()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_discount_input_form()
        basket_page.should_be_success_applying_discount()
