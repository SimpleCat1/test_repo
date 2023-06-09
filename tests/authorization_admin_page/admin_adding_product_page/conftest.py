from typing import Callable

import re

import allure
import pytest
from _pytest.fixtures import SubRequest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver
from tests.authorization_admin_page.admin_adding_product_page.admin_adding_product_page import (
    AdminAddingProductPage,
)
from tests.authorization_admin_page.admin_adding_product_page.admin_adding_product_locators import (
    AdminAddingProductLocators,
)


@pytest.fixture(scope='module')
def admin_adding_product(browser: WebDriver, request: SubRequest) -> AdminAddingProductPage:
    """
    Create a page class to get page methods.
    """
    def get_methods_page():
        return AdminAddingProductPage(browser, request)

    return get_methods_page()


@allure.step("Delete the created product in the admin panel.")
@pytest.fixture
def delete_product(
        admin_adding_product,
        request: SubRequest,
        intermediate_data: 'Data',
) -> Callable:
    """
    Delete the created product in the admin panel.

    I had to add a check that the alert disappeared, otherwise it turns out that the code runs
     too fast and the data does not have time to change on the web page
    """
    def _method(name_product: str) -> None:
        admin_adding_product.logger.info('deleting the created product from the admin panel')
        admin_adding_product.open_url(''.join((
            request.config.getoption("--url"),
            '/admin/index.php?route=catalog/product&user_token=',
            intermediate_data.token,
        )))
        admin_adding_product.click(
            AdminAddingProductPage.get_table_checkbox(name_product),
            'element_visibility',
        )
        admin_adding_product.click(AdminAddingProductLocators.button_delete_product)
        alert: Alert = admin_adding_product.alert_switch()
        alert.accept()

        assert admin_adding_product.alert_switch() is False

    return _method
