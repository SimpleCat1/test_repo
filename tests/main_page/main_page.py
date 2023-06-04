import allure

from tests.common_helper_ui import CommonHelperUi
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver


class MainPage(CommonHelperUi):

    def __init__(self, driver: WebDriver, request: FixtureRequest):
        super().__init__(driver, request)
        self.components_tab = ''.join((
            "//li/a[@href='",
            request.config.getoption("--url"),
            "/component']",
        ))
        self.components_tab_monitors = ''.join((
            "//li/a[@href='",
            request.config.getoption("--url"),
            "/component/monitor']",
        ))
        self.components_tab_mice_and_trackballs = ''.join((
            "//li/a[@href='",
            request.config.getoption("--url"),
            "/component/mouse']",
        ))

    @allure.step("changing the currency on the product page, on {currency}")
    def changing_currency(self, currency: str) -> None:
        """
        Change the currency on the main page.
        """
        self._log_create()
        self.click("//i[contains(@class,'fa-caret-down')]", 'element_visibility')
        self.click(f"//button[@name='{currency}']")

    @allure.step('We remove the product from the basket')
    def remove_item_from_shopping_cart(self) -> None:
        """
        Clears the cart of products on the main page.
        """
        self._log_create()
        self.element_invisibility('//div[@id="cart"]/ul/li/p')
        self.click('//button[contains(@class,"btn-inverse")]', 'element_visibility')
        self.click('//button[contains(@class,"btn-danger")]', 'element_visibility')
        self.element_presence_in_dom('//div[@id="cart"]/ul/li/p')
