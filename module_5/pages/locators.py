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

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK_NAME_ON_PAGE = (By.CSS_SELECTOR, 'div.product_main > h1')
    BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, 'p.price_color')
    INFO_BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(1) > div > strong')
    INFO_AMOUNT_OF_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(2) > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')

class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, 'span > [href="/ru/basket/"]')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.btn-primary.btn-block')
    BASKET_GOOD_ITEM = (By.CSS_SELECTOR, 'div.basket-items')
    BASKET_TOTAL_INFO = (By.CSS_SELECTOR, '#basket_totals')
    BASKET_VOUCHER_INFO = (By.CSS_SELECTOR, '#voucher_form_link')
    EMPTY_BASKET_RU_TEXT = (By.XPATH, '//p[contains(., \'Ваша корзина пуста.\')]')  #localization ru