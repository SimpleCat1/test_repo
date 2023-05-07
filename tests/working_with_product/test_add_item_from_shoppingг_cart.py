from typing import TYPE_CHECKING

import allure
import pytest

from tests.common_locators import CommonLocators

from tests.working_with_product.helper_ui import HelperUi
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from _pytest.fixtures import FixtureRequest


class TestAddItemFromShoppingCart(HelperUi):

    @pytest.mark.unparalleled
    def test_add_item(self, browser: 'WebDriver', request: 'FixtureRequest'):
        self.open_url(browser, request, request.config.getoption("--url"))
        self.click(
            browser,
            request,
            web_element=self.element_visibility(browser, request, CommonLocators.add_item),
        )

        with allure.step('Data verification'):
            alert_text = self.get_text_element(
                browser,
                request,
                web_element=self.element_visibility(browser, request, CommonLocators.allert),
            )
            text_added_product = self.get_text_element(
                browser,
                request,
                web_element=self.element_visibility(browser, request, CommonLocators.basket),
            )
            allure.attach(
                'Alert text',
                alert_text,
                allure.attachment_type.TEXT,
            )
            assert alert_text == 'Success: You have added MacBook to your shopping cart!\n×'
            assert text_added_product != '0 item(s) - $0.00'

        with allure.step('We return the settings to the previous ones'):
            self.remove_item_from_shopping_cart(browser, request)
