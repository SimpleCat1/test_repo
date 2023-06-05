from typing import TYPE_CHECKING

import allure
import pytest

from tests.main_page.main_page_locators import MainPageLocators
if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest
    from tests.main_page.main_page import MainPage


class TestRemovingItemFromShoppingCart:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_remove_item")
    @allure.description("Removing an item from the cart, if there is an item in the cart")
    @pytest.mark.unparalleled
    def test_remove_item(self, request: 'FixtureRequest', main_page: 'MainPage'):
        main_page.open_url(request.config.getoption("--url"))
        with allure.step('Adding the product to the cart'):
            main_page.click(MainPageLocators.add_item, 'element_visibility')

        with allure.step('Check that the item has been added to the cart'):
            main_page.element_invisibility(MainPageLocators.empty_basket)
            main_page.text_to_be_present(MainPageLocators.basket, '1 item(s) - $602.00')

        with allure.step('We remove the product from the basket'):
            main_page.remove_item_from_shopping_cart()

        with allure.step('Data verification'):
            alert_text = main_page.get_text_element(MainPageLocators.alert, 'element_visibility')
            text_remove_product = main_page.get_text_element(
                MainPageLocators.basket,
                'element_visibility',
            )
            allure.attach(alert_text, 'Alert text', allure.attachment_type.TEXT)
            allure.attach(text_remove_product, 'Basket text', allure.attachment_type.TEXT)
            assert alert_text == 'Success: You have added MacBook to your shopping cart!\n×'
            assert text_remove_product == '0 item(s) - $0.00'
