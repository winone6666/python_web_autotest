import pytest

from final.pages.review_page import ReviewPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/reviews/add/#addreview"


class TestUserDriveReview:
    @pytest.mark.xfail(reason='TODO Fix rating field and submit button')
    def test_user_can_add_review(self, browser):
        # Arrange
        page = ReviewPage(browser, link)
        page.open()
        # Assert
        page.should_be_review_page()
        # Act
        page.send_review()

    def test_user_can_cancel_writing_review(self, browser):
        # Arrange
        page = ReviewPage(browser, link)
        page.open()
        # Assert
        page.should_be_review_page()
        # Act
        page.cancel_writing_review()
