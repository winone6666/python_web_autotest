from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

main_page_link = 'http://selenium1py.pythonanywhere.com'

open_catalog_button_locator = '//ul[@data-navigation="dropdown-menu"]//following::a'
select_product_page_locator = '//article[@class="product_pod"]/following::h3[3]'
sbm_button_in_product_page_locator = '.btn.btn-lg.btn-primary.btn-add-to-basket'

def test_check_select_product_btn(browser):
    #Data
    sbm_button_text_ru = 'Добавить в корзину'
    sbm_button_text_en = 'Add to basket'
    sbm_button_text_es = 'Añadir al carrito'
    sbm_button_text_it = 'Aggiungi al carrello'

    try:
        #Arrange
        browser.get(main_page_link)
        open_catalog_button = browser.find_element(By.XPATH, open_catalog_button_locator)
        open_catalog_button.click()

        #Act
        select_product_page = browser.find_element(By.XPATH, select_product_page_locator)
        select_product_page.click()

        #Assert
        sbm_button_in_product_page = browser.find_element(By.CSS_SELECTOR, sbm_button_in_product_page_locator)
        select = Select(browser.find_element_by_tag_name("select"))
        if select.select_by_visible_text('Русский'):
            assert sbm_button_in_product_page.text == sbm_button_text_ru, \
                'The button text in not correct'
        if select.select_by_visible_text('British English'):
            assert sbm_button_in_product_page.text == sbm_button_text_en, \
                'The button text in not correct'
        if select.select_by_visible_text('español'):
            assert sbm_button_in_product_page.text == sbm_button_text_es, \
                'The button text in not correct'
        if select.select_by_visible_text('italiano'):
            assert sbm_button_in_product_page.text == sbm_button_text_it, \
                'The button text in not correct'

    finally:
        time.sleep(10)
        browser.quit()
