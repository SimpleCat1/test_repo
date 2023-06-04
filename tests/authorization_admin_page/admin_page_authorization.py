import allure
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver

from tests.authorization_admin_page.authorization_page_locators import AuthorizationPageLocators
from tests.main_page.main_page import MainPage


class AuthorizationAdminPage(MainPage):

    def __init__(self, driver: WebDriver, request: FixtureRequest):
        super().__init__(driver, request)

    def open_url_registration_page(self) -> None:
        url_for_open = ''.join((self.request.config.getoption("--url"), '/admin'))
        if self.driver.current_url != url_for_open:
            self.open_url(url_for_open)

    def authorization(self, username: str, password: str) -> None:
        with allure.step('authorization by pressing "Login"'):
            self.data_entry(username, AuthorizationPageLocators.username)
            self.data_entry(password, AuthorizationPageLocators.password)
            self.click(AuthorizationPageLocators.button_login)
