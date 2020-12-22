import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

language_list = ["ru", "en", "es", "it"]

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose user language, please: ru, en, es, it")
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    option = Options()
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=option)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=option)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.maximize_window()
    if browser_language in language_list:
        option.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        print("\nstart chrome browser for test..")
    else:
            raise pytest.UsageError("--language can not be selected")
    yield browser
    print("\nquit browser..")
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    browser.save_screenshot('module_5\\screenshots\\screenshot-%s.png' % now)
    browser.quit()