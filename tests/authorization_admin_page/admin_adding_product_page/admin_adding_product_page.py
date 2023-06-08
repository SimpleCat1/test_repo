from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver

from tests.authorization_admin_page.admin_page_authorization import AuthorizationAdminPage


class AdminAddingProductPage(AuthorizationAdminPage):

    def __init__(self, driver: WebDriver, request: FixtureRequest):
        super().__init__(driver, request)
        self.products = ''.join((
            "//a[contains(@href,'",
            request.config.getoption("--url"),
            '/admin/index.php?route=catalog/product', "')]",
        ))

    @staticmethod
    def get_table_product_name(name_product: str) -> str:
        """
        find the product in the table by name and return the locator.
        """
        return f"//tbody/tr[1]/td[3][contains(text(),'{name_product}')]"

    @staticmethod
    def get_table_checkbox(name_product: str) -> str:
        """
        find the product in the table by name and return the checkbox locator.
        """
        return f"//tbody/tr[1]/td[3][contains(text(),'{name_product}')]/preceding-sibling::td/input"
