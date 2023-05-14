from typing import TYPE_CHECKING

import allure
from faker import Faker

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
        self.click(browser, request, CommonLocators.dropdown_my_account, 'element_visibility')
        self.click(browser, request, "//a[contains(@href,'index.php?route=account/register')]", 'element_visibility')


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
        with allure.step('Entering data for user registration and clicking the "accept" button'):
            self.data_entry(
                browser,
                request,
                'asdf',
                "//input[@id='input-firstname']",
                'element_visibility',
            )
            self.data_entry(
                browser,
                request,
                'asdf',
                "//input[@id='input-lastname']",
                'element_visibility',
            )
            self.data_entry(
                browser,
                request,
                Faker().providers[11].ascii_company_email(),
                "//input[@id='input-email']",
                'element_visibility',
            )
            self.data_entry(
                browser,
                request,
                '1111',
                "//input[@id='input-telephone']",
                'element_visibility',
            )
            self.data_entry(
                browser,
                request,
                '1111',
                "//input[@id='input-password']",
                'element_visibility',
            )
            self.data_entry(
                browser,
                request,
                '1111',
                "//input[@id='input-confirm']",
                'element_visibility',
            )
            self.click(browser, request, "//input[@type='checkbox']", 'element_visibility')
            self.click(
                browser,
                request,
                "//input[contains(@class,'btn-primary')]",
                'element_visibility',
            )

        with allure.step('Data verification'):
            allure.attach(
                'text in bread crumbs',
                self.get_text_element(browser, request, '//div/h1', 'element_visibility'),
                allure.attachment_type.TEXT,
            )
            assert self.get_text_element(
                browser,
                request,
                '//div/h1',
                'element_visibility',
            ) == 'Your Account Has Been Created!'
