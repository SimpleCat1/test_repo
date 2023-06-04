from typing import TYPE_CHECKING

import pytest
from _pytest.fixtures import SubRequest
from tests.authorization_admin_page.admin_page_authorization import AuthorizationAdminPage
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.opera.webdriver import WebDriver


@pytest.fixture(scope='module')
def admin_authorization_page(browser: 'WebDriver', request: SubRequest) -> AuthorizationAdminPage:
    """
    Create a page class to get page methods.
    """
    def get_methods_page():
        return AuthorizationAdminPage(browser, request)

    return get_methods_page()
