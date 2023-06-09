from typing import Union

import allure
import faker
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver

from tests.main_page.main_page import MainPage
from tests.main_page.user_registration_page.registration_locators import (
    RegistrationLocators,
)


class RegistrationPage(MainPage):

    def __init__(self, driver: WebDriver, request: FixtureRequest):
        super().__init__(driver, request)

    def open_url_registration_page(self) -> None:
        """
        Go to the page if the page is different.
        """
        url_for_open = ''.join((
            self.request.config.getoption("--url"),
            RegistrationLocators.url_page,
        ))
        self.check_need_url(url_for_open)

    @allure.step('User registration')
    def user_registration(
            self,
            password: Union[str, int],
            password_confirm: Union[str, int],
            first_name: Union[str, int] = None,
            last_name: Union[str, int] = None,
            e_mail: Union[str, int] = None,
            telephone: Union[str, int] = None,
    ) -> None:
        """
        User registration.

        Enter the data in the fields on the registration page.
        """
        first_name: Union[str, int] = first_name or faker.Faker().providers[6].first_name()
        last_name: Union[str, int] = last_name or faker.Faker().providers[6].last_name()
        e_mail: Union[str, int] = e_mail or faker.Faker().providers[11].ascii_email()
        telephone: Union[str, int] = telephone or faker.Faker().providers[5].phone_number()

        self.data_entry(first_name, RegistrationLocators.first_name, 'element_visibility')
        self.data_entry(last_name, RegistrationLocators.last_name, 'element_visibility')
        self.data_entry(e_mail, RegistrationLocators.e_mail, 'element_visibility')
        self.data_entry(telephone, RegistrationLocators.telephone, 'element_visibility')
        self.data_entry(password, RegistrationLocators.password, 'element_visibility')
        self.data_entry(
            password_confirm,
            RegistrationLocators.password_confirm,
            'element_visibility',
        )
        if (
            not self.driver.find_element_by_xpath(
                RegistrationLocators.privacy_policy,
            ).is_selected()
        ):
            self.click(RegistrationLocators.privacy_policy, 'element_visibility')
        self.click(RegistrationLocators.button_continue, 'element_visibility')
        allure.attach(
            f"""
            <html>
                <head>
                    <p>
                      Data that was sent during registration
                    </p>
                </head>
            <body>
                <p>
                  first_name: {first_name}
                </p>
                <p>
                  last_name: {last_name}
                </p>
                <p>
                  e_mail: {e_mail}
                </p>
                <p>
                  telephone: {telephone}
                </p>
                <p>
                  password: {password}
                </p>
                <p>
                  password_confirm: {password_confirm}
                </p>
            </body>
            </html>
            """,
            "HTML attachment",
            allure.attachment_type.HTML,
        )
        self.logger.info(
            f'Data that was sent during registration: first_name: {first_name},'
            f' last_name: {last_name}, e_mail: {e_mail}, telephone: {telephone},'
            f' password: {password}, password_confirm: {password_confirm}'
        )
