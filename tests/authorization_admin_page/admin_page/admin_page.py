from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver

from tests.authorization_admin_page.admin_page_authorization import AuthorizationAdminPage


class AdminPage(AuthorizationAdminPage):

    def __init__(self, driver: WebDriver, request: FixtureRequest):
        super().__init__(driver, request)
        self.products = ''.join((
            "//a[contains(@href,'",
            request.config.getoption("--url"),
            '/admin/index.php?route=catalog/product', "')]",
        ))
