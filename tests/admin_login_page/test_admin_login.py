from typing import TYPE_CHECKING

import allure

from tests.common_locators import CommonLocators
from tests.common_helper_ui import CommonHelperUi
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from _pytest.fixtures import FixtureRequest


class TestAdminLogin(CommonHelperUi):

    def test_admin_login_page(self, browser: 'WebDriver', request: 'FixtureRequest'):
        self.open_url(browser, request, request.config.getoption("--url"))
        with allure.step('Go to the registration page via the "My Account" drop-down list'):
            self.click(browser, request, CommonLocators.dropdown_my_account, 'element_visibility')
            self.click(
                browser,
                request,
                "//a[contains(@href,'index.php?route=account/login')]",
                'element_visibility',
            )

        with allure.step('Data verification'):
            allure.attach(
                'Heading',
                "//div[@class='well']/a[contains(@class,'btn')]/ancestor::div/h2",
                allure.attachment_type.TEXT,
            )
            assert self.get_text_element(
                browser,
                request,
                "//div[@class='well']/a[contains(@class,'btn')]/ancestor::div/h2",
            ) == 'New Customer'
