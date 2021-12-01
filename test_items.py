# https://stepik.org/lesson/237240/step/9?unit=209628
# pytest -v -s --tb=line --browser_name=chrome --language=es test_items.py
# pytest -s --language=en_gb test_items.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def test_button_add_to_basket(browser, request):
    language = request.config.getoption('language')
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    except NoSuchElementException:
        assert False, 'Button not found'
