from typing import TYPE_CHECKING, Optional

import allure
from faker import Faker
from selenium.webdriver.remote.webelement import WebElement

from tests.common_locators import CommonLocators
from tests.common_helper_ui import CommonHelperUi
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from _pytest.fixtures import FixtureRequest


class TestUserRegistrationPage(CommonHelperUi):

    def test_user_registration_page(self, browser: 'WebDriver', request: 'FixtureRequest'):
        self.open_url(
            browser,
            request,
            f'{request.config.getoption("--url")}/index.php?route=account/register',
        )
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
                "//a[contains(@href,'index.php?route=account/register')]",
            )
        )

        with allure.step('Data verification'):
            heading: str = self.get_text_element(browser, request, "//div[@id='content']/h1")
            allure.attach(
                'Heading',
                heading,
                allure.attachment_type.TEXT,
            )
            assert heading == 'Register Account'

    def test_user_registration(self, browser: 'WebDriver', request: 'FixtureRequest'):
        self.open_url(
            browser,
            request,
            f'{request.config.getoption("--url")}/index.php?route=account/register',
        )
        self.data_entry(
            browser,
            request,
            'asdf',
            web_element=self.element_visibility(browser, request, "//input[@id='input-firstname']"),
        )
        self.data_entry(
            browser,
            request,
            'asdf',
            web_element=self.element_visibility(browser, request, "//input[@id='input-lastname']"),
        )
        self.data_entry(
            browser,
            request,
            Faker().providers[11].ascii_company_email(),
            web_element=self.element_visibility(browser, request, "//input[@id='input-email']"),
        )
        self.data_entry(
            browser,
            request,
            '1111',
            web_element=self.element_visibility(browser, request, "//input[@id='input-telephone']"),
        )
        self.data_entry(
            browser,
            request,
            '1111',
            web_element=self.element_visibility(browser, request, "//input[@id='input-password']"),
        )
        self.data_entry(
            browser,
            request,
            '1111',
            web_element=self.element_visibility(browser, request, "//input[@id='input-confirm']"),
        )
        self.click(
            browser,
            request,
            web_element=self.element_visibility(
                browser,
                request,
                "//input[@type='checkbox']",
            )
        )
        self.click(
            browser,
            request,
            web_element=self.element_visibility(
                browser,
                request,
                "//input[contains(@class,'btn-primary')]",
            )
        )

        with allure.step('Data verification'):
            text_bread_crumbs: Optional[WebElement] = (
                self.element_visibility(browser, request, "//div/h1")
            )
            allure.attach(
                'text in bread crumbs',
                self.get_text_element(
                    browser,
                    request,
                    web_element=text_bread_crumbs,
                ),
                allure.attachment_type.TEXT,
            )
            assert self.get_text_element(
                browser,
                request,
                web_element=text_bread_crumbs,
            ) == 'Your Account Has Been Created!'
