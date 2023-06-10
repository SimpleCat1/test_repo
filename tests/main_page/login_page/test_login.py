from typing import TYPE_CHECKING

import allure

from tests.main_page.login_page.login_locators import LoginLocators
from tests.main_page.main_locators import MainLocators

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest
    from tests.main_page.main_page import MainPage


class TestLogin:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_login_page")
    @allure.description("The Login page is displayed when navigating through the tab")
    def test_login_page(
            self,
            request: 'FixtureRequest',
            main_page: 'MainPage',
    ):
        main_page.open_url(request.config.getoption("--url"))
        with allure.step('Go to the registration page via the "My Account" drop-down list'):
            main_page.click(MainLocators.dropdown_my_account, 'element_visibility')
            main_page.click(MainLocators.dropdown_my_account_login, 'element_visibility')

        with allure.step('Data verification'):
            header_customer: str = main_page.get_text_element(LoginLocators.header_customer)
            allure.attach(header_customer, 'header customer', allure.attachment_type.TEXT)
            assert header_customer == 'New Customer'
