from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    EMAIL_INPUT_SIGN_UP = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_INPUT_SIGN_UP = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_CONFIRMED_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    SIGN_UP_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')
    EMAIL_IMPUT_SIGN_IN = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_INPUT_SIGN_IN = (By.CSS_SELECTOR, '#id_login-password')
    SIGN_IN_BTN = (By.CSS_SELECTOR, '[name="login_submit"]')
