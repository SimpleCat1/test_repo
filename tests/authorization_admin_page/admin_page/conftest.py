from typing import TYPE_CHECKING

import pytest
from _pytest.fixtures import SubRequest
from tests.authorization_admin_page.admin_page.admin_page import AdminPage
from tests.authorization_admin_page.admin_page.authorization_page_locators import AdminPageLocators
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.opera.webdriver import WebDriver


@pytest.fixture(scope='module')
def admin_page(browser: 'WebDriver', request: SubRequest) -> AdminPage:
    """
    Create a page class to get page methods.
    """
    def get_methods_page():
        return AdminPage(browser, request)

    return get_methods_page()


@pytest.fixture
def delete_product(admin_page: AdminPage) -> None:
    """
    Delete the created product in the admin panel.
    """
    yield
    admin_page.click(AdminPageLocators.table_checkbox, 'element_visibility')
    admin_page.click(AdminPageLocators.button_delete_product)
    alert = admin_page.driver.switch_to.alert
    alert.accept()
