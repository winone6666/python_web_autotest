from final.pages.review_page import ReviewPage
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/reviews/add/#addreview"

class TestUserDriveReview:
    @pytest.mark.xfail(reason='TODO Fix rating field and submit button')
    def test_user_can_add_review(self, browser):
        page = ReviewPage(browser, link)
        page.open()
        page.should_be_review_page()
        page.send_review()

    def test_user_can_cancel_writing_review(self, browser):
        page = ReviewPage(browser, link)
        page.open()
        page.should_be_review_page()
        page.cancel_writing_review()