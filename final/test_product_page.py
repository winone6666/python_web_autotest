import pytest

from final.pages.login_page import LoginPage
from final.pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


class TestProductPage:
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              ])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.open_math_alert()
        page.solve_quiz_and_get_code()
        page.should_be_equal_product_name_in_basket()
        page.should_be_equal_amount_in_basket()


class TestUserAddProductToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user("sun", "Ololoshkin2020")
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.open_math_alert()
        page.solve_quiz_and_get_code()
        page.should_be_equal_product_name_in_basket()
        page.should_be_equal_amount_in_basket()