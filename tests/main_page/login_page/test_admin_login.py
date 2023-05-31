from typing import TYPE_CHECKING

import allure
import pytest

from tests.main_page.login_page.login_page_locators import LoginPageLocators
from tests.main_page.main_page_locators import MainPageLocators

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest
    from tests.main_page.main_page import MainPage
    from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.mark.usefixtures("main_page")
class TestAdminLogin:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_admin_login_page")
    @allure.description("The Login page is displayed when navigating through the tab")
    def test_admin_login_page(
            self,
            browser: 'WebDriver',
            request: 'FixtureRequest',
            main_page: 'MainPage',
    ):
        main_page.open_url(request.config.getoption("--url"))
        with allure.step('Go to the registration page via the "My Account" drop-down list'):
            main_page.click(MainPageLocators.dropdown_my_account, 'element_visibility')
            main_page.click(MainPageLocators.dropdown_my_account_login, 'element_visibility')

        with allure.step('Data verification'):
            allure.attach('Heading', LoginPageLocators.header_customer, allure.attachment_type.TEXT)
            assert main_page.get_text_element(LoginPageLocators.header_customer) == 'New Customer'