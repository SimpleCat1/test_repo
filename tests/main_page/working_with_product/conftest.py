import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver

from tests.main_page.main_page import MainPage


@pytest.fixture(scope='class')
def return_default_bucket_state(browser: WebDriver, main_page: MainPage) -> None:
    """
    We are returning the bucket settings to the default state.
    """
    yield
    main_page.remove_item_from_shopping_cart()
