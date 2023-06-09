import re
from typing import TYPE_CHECKING, Callable

import allure
import pytest

import settings
from tests.authorization_admin_page.admin_adding_product_page.admin_adding_product_locators import (
    AdminAddingProductLocators,
)
from tests.authorization_admin_page.admin_page.admin_locators import AdminLocators
from tests.authorization_admin_page.admin_adding_product_page.admin_adding_product_page import (
    AdminAddingProductPage,
)

if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.opera.webdriver import WebDriver


@pytest.fixture(scope='class')
def intermediate_data() -> 'Data':
    """Intermediate data.

    This is the data that we get during the tests and they are used in other tests."""

    class Data:
        token: str

    return Data()


class TestAddingProductAdmin:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_product_creation")
    @allure.description("creating a product from the admin panel")
    def test_product_creation(
            self,
            browser: 'WebDriver',
            admin_adding_product: 'AdminAddingProductPage',
            delete_product: Callable,
            intermediate_data: 'Data',
    ):
        admin_adding_product.open_url_registration_page()
        admin_adding_product.authorization(settings.USER, settings.PASSWORD)

        with allure.step('product creation'):
            admin_adding_product.click(AdminLocators.catalog, 'element_visibility')
            admin_adding_product.click(admin_adding_product.products, 'element_visibility')
            admin_adding_product.click(
                AdminAddingProductLocators.add_new_product,
                'element_visibility',
            )
            admin_adding_product.data_entry(
                '12',
                AdminAddingProductLocators.product_name,
                'element_visibility',
            )
            admin_adding_product.data_entry('12', AdminAddingProductLocators.meta_tag_title)
            admin_adding_product.click(AdminAddingProductLocators.tab_data)
            admin_adding_product.data_entry(
                '12',
                AdminAddingProductLocators.model,
                'element_visibility',
            )
            admin_adding_product.click(AdminAddingProductLocators.save_button)

        with allure.step('Data verification'):
            name_product: str = admin_adding_product.get_text_element(
                AdminAddingProductPage.get_table_product_name('12'),
            )
            allure.attach(
                name_product,
                'the product name is displayed as:',
                allure.attachment_type.TEXT,
            )
            assert name_product == '12'

        intermediate_data.token = re.search(
            '(?<=user_token=).*',
            admin_adding_product.driver.current_url,
        ).group()
        delete_product('12')
