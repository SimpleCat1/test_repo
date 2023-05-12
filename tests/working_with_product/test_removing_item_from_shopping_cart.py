from typing import TYPE_CHECKING

import allure
import pytest

from tests.common_locators import CommonLocators
from tests.working_with_product.helper_ui import HelperUi
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from _pytest.fixtures import FixtureRequest


class TestRemovingItemFromShoppingCart(HelperUi):

    @pytest.mark.unparalleled
    def test_remove_item(self, browser: 'WebDriver', request: 'FixtureRequest'):
        self.open_url(browser, request, request.config.getoption("--url"))
        with allure.step('Adding the product to the cart'):
            self.click(browser, request, CommonLocators.add_item, 'element_visibility')

        with allure.step('Check that the item has been added to the cart'):
            self.element_invisibility(browser, request, '//div[@id="cart"]/ul/li/p')
            self.text_to_be_present(browser, request, CommonLocators.basket, '1 item(s) - $602.00')

        with allure.step('We remove the product from the basket'):
            self.remove_item_from_shopping_cart(browser, request)

        with allure.step('Data verification'):
            alert_text = self.get_text_element(
                browser,
                request,
                CommonLocators.allert,
                'element_visibility',
            )
            text_remove_product = self.get_text_element(
                browser,
                request,
                CommonLocators.basket,
            )
            allure.attach('Alert text', alert_text, allure.attachment_type.TEXT)
            allure.attach('Basket text', text_remove_product, allure.attachment_type.TEXT)
            assert alert_text == 'Success: You have added MacBook to your shopping cart!\n×'
            assert text_remove_product == '0 item(s) - $0.00'
