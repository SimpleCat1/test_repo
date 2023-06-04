from typing import TYPE_CHECKING

import allure
import pytest

from tests.main_page.main_page import MainPage
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.opera.webdriver import WebDriver


@pytest.fixture
def return_default_currency_settings(browser: 'WebDriver', main_page: MainPage) -> None:
    """
    Return the currency to the default value.
    """
    yield
    with allure.step('We return the currency settings to default'):
        main_page.changing_currency('USD')
