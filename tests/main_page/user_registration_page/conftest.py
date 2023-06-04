from typing import TYPE_CHECKING

import pytest
from _pytest.fixtures import SubRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.main_page.main_page_locators import MainPageLocators
from tests.main_page.user_registration_page.registration_page import RegistrationPage
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.opera.webdriver import WebDriver


@pytest.fixture(scope='module')
def registration_page(browser: 'WebDriver', request: SubRequest) -> RegistrationPage:
    """
    Create a page class to get page methods.
    """
    def get_methods_page():
        return RegistrationPage(browser, request)

    return get_methods_page()


@pytest.fixture
def logout(registration_page: RegistrationPage) -> None:
    """
    Log out of the authorized account.
    """
    yield
    element_found: bool = (
        WebDriverWait(registration_page.driver, 5).until(EC.invisibility_of_element_located((
            By.XPATH,
            MainPageLocators.dropdown_my_account_logout,
        )))
    )
    if isinstance(element_found, WebElement):
        registration_page.click(MainPageLocators.dropdown_my_account, 'element_visibility')
        registration_page.click(MainPageLocators.dropdown_my_account_logout, 'element_visibility')
