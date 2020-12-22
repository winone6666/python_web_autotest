from .base_page import BasePage
from .locators import ResetPasswordPageLocators
from .locators import BasePageLocators

class ResetPasswordPage(BasePage):
    def should_be_password_reset_url(self):
        login_url = self.browser.current_url
        assert "password-reset" in login_url, 'No word-combination "password-reset" in current url'

    def should_be_reset_password_form(self):
        assert self.is_element_present(*ResetPasswordPageLocators.EMAIL_INPUT_RESET), 'No email field'
        assert self.is_element_present(*ResetPasswordPageLocators.SEND_PASSWORD_EMAIL_BTN), 'No send button'

    def should_be_reset_password_page(self):
        self.should_be_password_reset_url()
        self.should_be_reset_password_form()

    def should_be_send_message_to_reset_password(self, email):
        self.browser.find_element(*ResetPasswordPageLocators.EMAIL_INPUT_RESET).send_keys(email)
        self.browser.find_element(*ResetPasswordPageLocators.SEND_PASSWORD_EMAIL_BTN).click()
        assert self.is_element_present(*ResetPasswordPageLocators.SUCCESS_MESSAGE_SENT_EMAIL)