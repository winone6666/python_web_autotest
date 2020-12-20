from .base_page import BasePage
from .locators import ReviewPageLocators
from .locators import BasePageLocators

class ReviewPage(BasePage):
    def should_be_review_url(self):
        login_url = self.browser.current_url
        assert "reviews/add/#addreview" in login_url, 'No words "reviews/add/#addreview" in current url'

    def should_be_review_form(self):
        assert self.is_element_present(*ReviewPageLocators.TITLE_INPUT), 'No title field'
        assert self.is_element_present(*ReviewPageLocators.PRODUCT_RATING), 'No product rating field'
        assert self.is_element_present(*ReviewPageLocators.MESSAGE_INPUT), 'No message field'
        assert self.is_element_present(*ReviewPageLocators.NAME_INPUT), 'No name fild'
        assert self.is_element_present(*ReviewPageLocators.EMAIL_INPUT), 'No email field'
        assert self.is_element_present(*ReviewPageLocators.SAVE_REVIEW_BTN), 'No save button'
        assert self.is_element_present(*ReviewPageLocators.CANCEL_REVIEW_BTN), 'No cancel button'

    def should_be_review_page(self):
        self.should_be_review_url(()
        self.should_be_review_form()

    def write_review(self):
        #Data
        title = 'One book name'
        message = 'Text for review to check'
        name = 'User User'
        email = 'user@user.user'
        #Arrange
        self.browser.find_element(*ReviewPageLocators.TITLE_INPUT).send_keys(title)
        self.browser.find_element(*ReviewPageLocators.MESSAGE_INPUT).send_keys(message)
        self.browser.find_element(*ReviewPageLocators.NAME_INPUT).send_keys(name)
        self.browser.find_element(*ReviewPageLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*ReviewPageLocators.PRODUCT_RATING).click()

    def send_review(self):
        self.write_review()
        self.browser.find_element(*ReviewPageLocators.SAVE_REVIEW_BTN).click()
        assert self.is_element_present(*ReviewPageLocators.SUCCESS_MESSAGE), 'The review is not saved'

    def cancel_writing_review(self):
        self.write_review()
        self.browser.find_element(*ReviewPageLocators.CANCEL_REVIEW_BTN).click()
        assert not self.should_be_review_url()





