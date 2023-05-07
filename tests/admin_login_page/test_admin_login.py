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
        self.click(
            browser,
            request,
            web_element=self.element_visibility(
                browser,
                request,
                CommonLocators.dropdown_my_account,
            ),
        )
        self.click(
            browser,
            request,
            web_element=self.element_visibility(
                browser,
                request,
                "//a[contains(@href,'index.php?route=account/login')]",
            ),
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
