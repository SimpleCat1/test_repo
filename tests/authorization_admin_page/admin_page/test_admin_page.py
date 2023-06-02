from typing import TYPE_CHECKING

import allure
import pytest

from tests.authorization_admin_page.admin_page.authorization_page_locators import AdminPageLocators
from tests.authorization_admin_page.authorization_page_locators import AuthorizationPageLocators

if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from tests.authorization_admin_page.admin_page.admin_page import AdminPage


class TestUserRegistrationPage:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_user_registration_page")
    @allure.description("The registration header is specified")
    def test_authorization_admin(
            self,
            browser: 'WebDriver',
            admin_page: 'AdminPage',
            delete_product: 'None',
    ):
        admin_page.open_url_registration_page()
        admin_page.data_entry('user', AuthorizationPageLocators.username)
        admin_page.data_entry('bitnami', AuthorizationPageLocators.password)
        admin_page.click(AuthorizationPageLocators.button_login)
        admin_page.click(AdminPageLocators.catalog, 'element_visibility')
        admin_page.click(admin_page.products, 'element_visibility')
        admin_page.click(AdminPageLocators.add_new_product, 'element_visibility')
        admin_page.data_entry('12', AdminPageLocators.product_name, 'element_visibility')
        admin_page.data_entry('12', AdminPageLocators.meta_tag_title)
        admin_page.click(AdminPageLocators.tab_data)
        admin_page.data_entry('12', AdminPageLocators.model, 'element_visibility')
        admin_page.click(AdminPageLocators.save_button)

        with allure.step('Data verification'):
            name_product: str = admin_page.get_text_element(AdminPageLocators.table_product_name)
            assert name_product == '12'
            allure.attach(
                'the product name is displayed as:',
                name_product,
                allure.attachment_type.TEXT,
            )
