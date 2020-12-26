import random

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_SIGN_UP)
        email_input.send_keys(email + str(random.randint(10000, 20000000)) + "@ololo.com")
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_SIGN_UP)
        password_input.send_keys("Ololoshkin2020")
        password_confirmed_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRMED_INPUT)
        password_confirmed_input.send_keys(password)
        submit_btn = self.browser.find_element(*LoginPageLocators.SIGN_UP_BTN)
        submit_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, 'No word "login" in current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_IMPUT_SIGN_IN), 'No email field'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_SIGN_IN), 'No password field'
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_BTN), 'No submit button'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_INPUT_SIGN_UP), 'No email field'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_SIGN_UP), 'No password field'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_CONFIRMED_INPUT), 'No confirmed password field'
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_BTN), 'No submit button'
