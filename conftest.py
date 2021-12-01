import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox or opera')
    parser.addoption('--language', action='store', default='ru', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if (browser_name == 'chrome'):
        print('\nStart Chrome browser for test ...')
        browser = webdriver.Chrome()
    elif (browser_name == 'firefox'):
        print('\nStart Firefox browser for test ...')
        browser = webdriver.Firefox()
    elif (browser_name == 'opera'):
        print('\nStart Opera browser for test ...')
        browser = webdriver.Opera()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox or opera')
    yield browser
    print('\nQuit browser ...')
    browser.quit()
