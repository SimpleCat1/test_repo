import allure

from tests.common_helper_ui import CommonHelperUi
from selenium.webdriver.chrome.webdriver import WebDriver
from _pytest.fixtures import FixtureRequest


class HelperUi(CommonHelperUi):

    @allure.step("changing the currency on the product page, on {currency}")
    def changing_currency(self, browser: WebDriver, request: FixtureRequest, currency: str) -> None:
        self._log_create(request)
        self.click(browser, request, "//i[contains(@class,'fa-caret-down')]", 'element_visibility')
        self.click(browser, request, f"//button[@name='{currency}']")
