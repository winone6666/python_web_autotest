from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, 'No word "login" in current url'
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_IMPUT_SIGN_IN), 'No email field'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_SIGN_IN), 'No password field'
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_BTN), 'No submit button'
        # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_INPUT_SIGN_UP), 'No email field'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_SIGN_UP), 'No password field'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_CONFIRMED_INPUT), 'No confirmed password field'
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_BTN), 'No submit button'
        # реализуйте проверку, что есть форма регистрации на странице
