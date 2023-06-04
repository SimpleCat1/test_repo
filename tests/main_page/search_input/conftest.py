from typing import TYPE_CHECKING

import pytest
from _pytest.fixtures import SubRequest

from tests.main_page.search_input.search_page import SearchPage
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.opera.webdriver import WebDriver


@pytest.fixture(scope='module')
def search_page(browser: 'WebDriver', request: SubRequest) -> SearchPage:
    """
    Create a page class to get page methods.
    """
    def get_methods_page():
        return SearchPage(browser, request)

    return get_methods_page()
