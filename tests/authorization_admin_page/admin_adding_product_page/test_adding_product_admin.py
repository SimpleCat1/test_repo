from typing import TYPE_CHECKING, Callable

import allure

import settings
from tests.authorization_admin_page.admin_adding_product_page.admin_adding_product_locators import AdminAddingProductLocators
from tests.authorization_admin_page.admin_adding_product_page.admin_adding_product_page import AdminAddingProductPage

if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.opera.webdriver import WebDriver


class TestAddingProductAdmin:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_product_creation")
    @allure.description("creating a product from the admin panel")
    def test_product_creation(
            self,
            browser: 'WebDriver',
            admin_page: AdminAddingProductPage,
            delete_product: Callable,
    ):
        admin_page.open_url_registration_page()
        admin_page.authorization(settings.USER, settings.PASSWORD)

        with allure.step('product creation'):
            admin_page.click(AdminAddingProductLocators.catalog, 'element_visibility')
            admin_page.click(admin_page.products, 'element_visibility')
            admin_page.click(AdminAddingProductLocators.add_new_product, 'element_visibility')
            admin_page.data_entry('12', AdminAddingProductLocators.product_name, 'element_visibility')
            admin_page.data_entry('12', AdminAddingProductLocators.meta_tag_title)
            admin_page.click(AdminAddingProductLocators.tab_data)
            admin_page.data_entry('12', AdminAddingProductLocators.model, 'element_visibility')
            admin_page.click(AdminAddingProductLocators.save_button)

        with allure.step('Data verification'):
            name_product: str = admin_page.get_text_element(AdminAddingProductPage.get_table_product_name('12'))
            allure.attach(
                name_product,
                'the product name is displayed as:',
                allure.attachment_type.TEXT,
            )
            assert name_product == '12'

        delete_product('12')
