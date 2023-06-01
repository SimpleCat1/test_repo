from typing import TYPE_CHECKING

import allure
import pytest

from tests.authorization_admin_page.authorization_page_locators import AuthorizationPageLocators
from tests.authorization_admin_page.parametrization_admin_authorization import (
    ParametrizationAdminAuthorization,
)

if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from tests.authorization_admin_page.admin_page_authorization import AuthorizationAdminPage


@pytest.mark.usefixtures("admin_authorization_page")
class TestAdminPage:

    @pytest.mark.parametrize(
        "data",
        ParametrizationAdminAuthorization.input_data,
        ids=[unit.name for unit in ParametrizationAdminAuthorization.input_data],
    )
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_user_registration_page")
    @allure.description("The registration header is specified")
    def test_incorrect_authorization(
            self,
            browser: 'WebDriver',
            admin_authorization_page: 'AuthorizationAdminPage',
            data: 'data_tuple',
    ):
        admin_authorization_page.open_url_registration_page()
        admin_authorization_page.data_entry(data.username, AuthorizationPageLocators.username)
        admin_authorization_page.data_entry(data.password, AuthorizationPageLocators.password)
        admin_authorization_page.click(AuthorizationPageLocators.button_login)

        with allure.step('Data verification'):
            alert: str = admin_authorization_page.get_text_element(
                AuthorizationPageLocators.alert_authorization,
            )
            assert alert == 'No match for Username and/or Password.'
            allure.attach(
                'authorization alert',
                alert,
                allure.attachment_type.TEXT,
            )
