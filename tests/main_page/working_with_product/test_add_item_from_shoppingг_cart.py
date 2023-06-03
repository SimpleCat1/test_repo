from typing import TYPE_CHECKING

import allure
import pytest

from tests.main_page.main_page_locators import MainPageLocators

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest
    from tests.main_page.main_page import MainPage


class TestAddItemFromShoppingCart:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_add_item")
    @allure.description("Adding an item to the cart")
    @pytest.mark.unparalleled
    def test_add_item(
            self,
            request: 'FixtureRequest',
            main_page: 'MainPage',
            return_default_bucket_state: 'None',
    ):
        main_page.open_url(request.config.getoption("--url"))
        with allure.step('Adding the product to the cart'):
            main_page.click(MainPageLocators.add_item, 'element_visibility')

        with allure.step('Data verification'):
            alert_text: str = main_page.get_text_element(
                MainPageLocators.alert,
                'element_visibility',
            )
            shopping_cart_text: bool = main_page.text_to_be_present(
                MainPageLocators.basket,
                '1 item(s) - $602.00',
            )
            allure.attach('Alert text', alert_text, allure.attachment_type.TEXT)
            allure.attach(
                'Alert text',
                'the cart has a product with the following data "1 item(s) - $602.00": '
                f'{shopping_cart_text}',
                allure.attachment_type.TEXT,
            )
            assert alert_text == 'Success: You have added MacBook to your shopping cart!\n×'
