from typing import TYPE_CHECKING

from _pytest.fixtures import FixtureRequest

from tests.authorization_admin_page.admin_page_authorization import AuthorizationAdminPage
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.opera.webdriver import WebDriver


class AdminPage(AuthorizationAdminPage):

    def __init__(self, driver: 'WebDriver', request: FixtureRequest):
        super().__init__(driver, request)
        self.products = ''.join((
            "//a[contains(@href,'",
            request.config.getoption("--url"),
            '/admin/index.php?route=catalog/product', "')]",
        ))
