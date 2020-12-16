import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

language_list = ["ru", "en-GB", "es", "it"]

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose user language, please: ru, en-GB, es, fr")

@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    option = Options()
    browser = webdriver.Chrome(options=option)
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