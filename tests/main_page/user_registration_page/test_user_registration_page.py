from typing import TYPE_CHECKING

import allure
import pytest
from faker import Faker

from tests.main_page.main_page_locators import MainPageLocators
from tests.main_page.user_registration_page.parametrization_registration_user import (
    ParametrizationRegistrationUser,
)
from tests.main_page.user_registration_page.registration_page_locators import (
    RegistrationPageLocators,
)
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from _pytest.fixtures import FixtureRequest
    from tests.main_page.main_page import MainPage
    from tests.main_page.user_registration_page.registration_page import RegistrationPage


@pytest.mark.usefixtures("main_page", "registration_page")
class TestUserRegistrationPage:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_user_registration_page")
    @allure.description("The registration header is specified")
    def test_user_registration_page(
            self,
            browser: 'WebDriver',
            request: 'FixtureRequest',
            main_page: 'MainPage',
    ):
        main_page.open_url(f'{request.config.getoption("--url")}')
        main_page.click(MainPageLocators.dropdown_my_account, 'element_visibility')
        main_page.click(MainPageLocators.dropdown_my_account_register, 'element_visibility')

        with allure.step('Data verification'):
            heading: str = main_page.get_text_element(RegistrationPageLocators.header_registration)
            allure.attach('Heading', heading, allure.attachment_type.TEXT)
            assert heading == 'Register Account'

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_user_registration")
    @allure.description("Registration of a new user")
    def test_user_registration(
            self,
            request: 'FixtureRequest',
            registration_page: 'RegistrationPage',
            logout: None,
    ):
        registration_page.open_url(''.join((
            request.config.getoption("--url"),
            RegistrationPageLocators.url_page,
        )))
        with allure.step('Entering data for user registration and clicking the "accept" button'):
            registration_page.user_registration('1111', '1111')

        with allure.step('Data verification'):
            allure.attach(
                'text in bread crumbs',
                registration_page.get_text_element(
                    RegistrationPageLocators.header_success_registration,
                    'element_visibility',
                ),
                allure.attachment_type.TEXT,
            )
            assert (
                    registration_page.get_text_element(
                        RegistrationPageLocators.header_success_registration,
                        'element_visibility',
                    )
                    == 'Your Account Has Been Created!'
            )

    @pytest.mark.parametrize(
        "data",
        ParametrizationRegistrationUser.user_name_incorrect,
        ids=[unit.name for unit in ParametrizationRegistrationUser.user_name_incorrect],
    )
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_user_registration")
    @allure.description("Registration of a new user")
    def test_user_registration_wrong_name(
            self,
            browser: 'WebDriver',
            request: 'FixtureRequest',
            registration_page: 'RegistrationPage',
            data: 'data_tuple',
            logout: None,
    ):
        registration_page.open_url_registration_page()
        with allure.step('Entering data for user registration and clicking the "accept" button'):
            registration_page.user_registration(
                data.password,
                data.password_confirm,
                data.first_name,
                data.last_name,
            )

        with allure.step('Data verification'):
            current_url: str = registration_page.driver.current_url
            allure.attach(
                'The URL of the registration page (there should not be a page of an already'
                ' authorized user)',
                current_url,
                allure.attachment_type.TEXT,
            )
            assert current_url == ''.join((
                request.config.getoption("--url"),
                '/index.php?route=account/success',
            ))

    @pytest.mark.parametrize(
        "data",
        ParametrizationRegistrationUser.input_data_errors_password,
        ids=[unit.name for unit in ParametrizationRegistrationUser.input_data_errors_password],
    )
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_user_registration")
    @allure.description("Registration of a new user")
    def test_registration_error_password(
            self,
            registration_page: 'RegistrationPage',
            data: 'data_tuple',
    ):
        registration_page.open_url_registration_page()
        with allure.step('Entering data for user registration and clicking the "accept" button'):
            registration_page.user_registration(data.password, data.password_confirm)

        with allure.step('Data verification'):
            allure.attach('popup Input errors', data.check, allure.attachment_type.TEXT)
            assert registration_page.text_to_be_present(
                RegistrationPageLocators.popup_error_password,
                data.check,
            )

    @pytest.mark.parametrize(
        "data",
        ParametrizationRegistrationUser.input_data_errors_password_confirm,
        ids=[
            unit.name for unit in ParametrizationRegistrationUser.input_data_errors_password_confirm
        ],
    )
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_user_registration")
    @allure.description("Registration of a new user")
    def test_registration_error_password_confirm(
            self,
            registration_page: 'RegistrationPage',
            data: 'data_tuple',
            logout: 'None',
    ):
        registration_page.open_url_registration_page()
        with allure.step('Entering data for user registration and clicking the "accept" button'):
            registration_page.user_registration(data.password, data.password_confirm)

        with allure.step('Data verification'):
            allure.attach('popup Input errors', data.check, allure.attachment_type.TEXT)
            assert registration_page.text_to_be_present(
                RegistrationPageLocators.popup_error_password_confirm,
                data.check,
            )

    @pytest.mark.parametrize(
        "data",
        ParametrizationRegistrationUser.input_data_errors_telephone,
        ids=[unit.name for unit in ParametrizationRegistrationUser.input_data_errors_telephone],
    )
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_user_registration")
    @allure.description("Registration of a new user")
    def test_registration_error_telephone(
            self,
            registration_page: 'RegistrationPage',
            data: 'data_tuple',
    ):
        registration_page.open_url_registration_page()
        with allure.step('Entering data for user registration and clicking the "accept" button'):
            registration_page.user_registration(
                data.password,
                data.password_confirm,
                telephone=data.telephone,
            )

        with allure.step('Data verification'):
            allure.attach('popup Input errors', data.check, allure.attachment_type.TEXT)
            assert registration_page.text_to_be_present(
                RegistrationPageLocators.popup_error_telephone,
                data.check,
            )

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_user_registration")
    @allure.description("Registration of a new user")
    def test_user_registration_wrong_email(
            self,
            request: 'FixtureRequest',
            registration_page: 'RegistrationPage',
    ):
        registration_page.open_url(''.join((
            request.config.getoption("--url"),
            RegistrationPageLocators.url_page,
        )))
        with allure.step('Entering data for user registration and clicking the "accept" button'):
            registration_page.user_registration('1111', '1111', e_mail='asdf')

        with allure.step('Data verification'):
            current_url: str = registration_page.driver.current_url
            allure.attach(
                'The URL of the registration page (there should not be a page of an already'
                ' authorized user)',
                current_url,
                allure.attachment_type.TEXT,
            )
            assert current_url == ''.join((
                request.config.getoption("--url"),
                '/index.php?route=account/register',
            ))
