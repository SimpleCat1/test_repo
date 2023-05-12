from typing import TYPE_CHECKING
import allure
import pytest
from tests.working_with_currency.helper_ui import HelperUi

if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from _pytest.fixtures import FixtureRequest


class TestChangCurrency(HelperUi):

    @pytest.mark.unparalleled
    def test_product_card(self, browser: 'WebDriver', request: 'FixtureRequest'):
        self.open_url(browser, request, request.config.getoption("--url"))
        with allure.step('Changed the currency on the main page'):
            self.changing_currency(browser, request, 'EUR')

        with allure.step('Data verification'):
            text_currency: str = self.get_text_element(browser, request, "//strong")
            allure.attach(
                'Text currency',
                text_currency,
                allure.attachment_type.TEXT,
            )
            assert text_currency == '€'

        with allure.step('We return the settings to the previous ones'):
            self.changing_currency(browser, request, 'USD')
