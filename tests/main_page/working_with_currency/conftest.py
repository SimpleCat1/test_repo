import allure
import pytest

from tests.main_page.main_page import MainPage

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver


@allure.step("Return the currency to the default value. (USD)")
@pytest.fixture
def return_default_currency_settings(browser: WebDriver, main_page: MainPage) -> None:
    """
    Return the currency to the default value.
    """
    yield
    main_page.logger.info('Return the currency to the default value. (USD)')
    main_page.changing_currency('USD')
