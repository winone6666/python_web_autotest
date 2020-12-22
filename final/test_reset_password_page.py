from final.pages.reset_password_page import ResetPasswordPage

link = "http://selenium1py.pythonanywhere.com/ru/password-reset/"

class TestUserResetPassword:
    def test_user_can_reset_password(self, browser):
        page = ResetPasswordPage(browser, link)
        page.open()
        page.should_be_reset_password_page()
        page.should_be_send_message_to_reset_password("user@user1214.user")