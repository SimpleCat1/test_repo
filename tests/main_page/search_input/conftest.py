import pytest
from _pytest.fixtures import SubRequest
from selenium.webdriver.chrome.webdriver import WebDriver

from tests.main_page.search_input.search_page import SearchPage


@pytest.fixture(scope='module')
def search_page(browser: WebDriver, request: SubRequest) -> SearchPage:
    """
    Create a page class to get page methods.
    """
    def get_methods_page():
        return SearchPage(browser, request)

    return get_methods_page()
