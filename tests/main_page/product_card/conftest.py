from typing import TYPE_CHECKING

import pytest
from _pytest.fixtures import SubRequest
from tests.main_page.working_with_product.conftest import return_default_bucket_state  # noqa F401
from tests.main_page.product_card.product_page import ProductPage
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.opera.webdriver import WebDriver


@pytest.fixture(scope='module')
def product_card_page(browser: 'WebDriver', request: SubRequest) -> ProductPage:
    """
    Create a page class to get page methods.
    """
    def get_methods_page():
        return ProductPage(browser, request)

    return get_methods_page()
