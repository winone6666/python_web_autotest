from selenium import webdriver
from selenium.webdriver.common.by import By

main_page_link = 'http://selenium1py.pythonanywhere.com/ru'

open_catalog_button_locator = '//a[contains(., \'Все товары\')]'
select_product_button_locator = '[data-loading-text="Добавление..."]'
info_book_name_in_basket_locator = '#messages div:nth-child(1) > div > strong'
info_success_benefit_offer_locator = '#messages div:nth-child(2) > div > strong'
info_sum_of_basket_locator = '#messages div:nth-child(2) > p > strong'
product_name_locator = '[title="The shellcoder\'s handbook"]'
product_amount_locator = '//a[@title="The shellcoder\'s handbook"]//following::p[1]'


def test_show_short_info_about_basket_filling():
    # Data
    text_success_benefit_offer = 'Deferred benefit offer'

    try:
        #Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        open_catalog_button = browser.find_element(By.XPATH, open_catalog_button_locator)
        open_catalog_button.click()

        #Act
        select_product_button = browser.find_element(By.CSS_SELECTOR, select_product_button_locator)
        select_product_button.click()

        #Assert
        product_name = browser.find_element(By.CSS_SELECTOR, product_name_locator).text
        product_amount = browser.find_element(By.XPATH, product_amount_locator).text
        product_name_in_message = browser.find_element(By.CSS_SELECTOR, info_book_name_in_basket_locator).text
        product_amount_in_message = browser.find_element(By.CSS_SELECTOR,info_sum_of_basket_locator).text
        info_success_benefit_offer_in_message = browser.find_element(By.CSS_SELECTOR, info_success_benefit_offer_locator).text
        assert product_name == product_name_in_message, \
            'Product name in message is not equal to product name'
        assert text_success_benefit_offer == info_success_benefit_offer_in_message, \
            'The offer condition is not convinient'
        assert product_amount == product_amount_in_message, \
            'Product amount in message is not equal to product amount'

    finally:
        browser.quit()

test_show_short_info_about_basket_filling()
