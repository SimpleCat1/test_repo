from typing import TYPE_CHECKING

from _pytest.fixtures import FixtureRequest

from tests.main_page.main_page import MainPage
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.opera.webdriver import WebDriver

class AuthorizationAdminPage(MainPage):

    def __init__(self, driver: 'WebDriver', request: FixtureRequest):
        super().__init__(driver, request)

    def open_url_registration_page(self) -> None:
        url_for_open = ''.join((self.request.config.getoption("--url"), '/admin'))
        if self.driver.current_url != url_for_open:
            self.open_url(url_for_open)
