import allure
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver

from tests.authorization_admin_page.authorization_locators import AuthorizationLocators
from tests.common_helper_ui import CommonHelperUi


class AuthorizationAdminPage(CommonHelperUi):

    def __init__(self, driver: WebDriver, request: FixtureRequest):
        super().__init__(driver, request)

    def open_url_registration_page(self) -> None:
        url_for_open = ''.join((self.request.config.getoption("--url"), '/admin'))
        self.check_need_url(url_for_open)

    @allure.step("authorization on the page username: {username}, password: {password}")
    def authorization(self, username: str, password: str) -> None:
        self.logger.info('authorization by pressing "Login"')
        with allure.step('authorization by pressing "Login"'):
            self.data_entry(username, AuthorizationLocators.username)
            self.data_entry(password, AuthorizationLocators.password)
            self.click(AuthorizationLocators.button_login)
