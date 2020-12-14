import pytest
from pytest import fixture
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@fixture
def browser(scope="module"):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


# вызываем фикстуру в тесте, передав ее как параметр
@pytest.mark.smoke
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


@pytest.mark.win10
@pytest.mark.regression
def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".basket-mini .btn-group > a")