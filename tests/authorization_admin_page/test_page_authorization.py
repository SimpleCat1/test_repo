from typing import TYPE_CHECKING

import allure
import pytest

from tests.authorization_admin_page.authorization_locators import AuthorizationLocators
from tests.authorization_admin_page.parametrization_admin_authorization import (
    ParametrizationAdminAuthorization,
)

if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from tests.authorization_admin_page.admin_page_authorization import AuthorizationAdminPage


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

        admin_authorization_page.authorization(data.username, data.password)

        with allure.step('Data verification'):
            alert: str = admin_authorization_page.get_text_element(
                AuthorizationLocators.alert_authorization,
            )
            allure.attach(
                alert,
                'authorization alert',
                allure.attachment_type.TEXT,
            )
            assert alert == 'No match for Username and/or Password.\n×'
