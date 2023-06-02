from typing import TYPE_CHECKING

import allure
import pytest

from tests.main_page.main_page_locators import MainPageLocators
from tests.main_page.product_card.parametrization_card_product import ParametrizationCardProduct
from tests.main_page.product_card.product_page_locators import ProductPageLocators

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest
    from tests.main_page.main_page import MainPage


class TestProductCard:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_product_card")
    @allure.description("The title of the product catalog is displayed")
    def test_product_card(self, request: 'FixtureRequest', main_page: 'MainPage'):
        main_page.open_url(request.config.getoption("--url"))
        with allure.step('Clicked on the product'):
            main_page.click(MainPageLocators.first_product, 'element_visibility')

        with allure.step('Data verification'):
            name_product: str = main_page.get_text_element(ProductPageLocators.header_product)
            allure.attach('Name product', name_product, allure.attachment_type.TEXT)
            assert name_product == 'MacBook'

    @pytest.mark.parametrize(
        "data",
        ParametrizationCardProduct.input_data,
        ids=[unit.name for unit in ParametrizationCardProduct.input_data],
    )
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_adding_product_from_product_card")
    @allure.description("adding a product from the product card (negative and positive cases)")
    def test_adding_product_from_product_card(
            self,
            product_card_page: 'ProductPage',
            data: 'data_tuple',
            return_default_bucket_state: 'None',
    ):
        product_card_page.open_url_card_page('macbook')

        with allure.step('Data verification'):
            cost_of_product: float = product_card_page.adding_quantity_of_product(data.count_product)

        with allure.step('Data verification'):
            alert_text: str = product_card_page.get_text_element(
                MainPageLocators.alert,
                'element_visibility',
            )
            text_remove_product: str = product_card_page.get_text_element(
                MainPageLocators.basket,
                'element_visibility',
            )
            allure.attach('Alert text', alert_text, allure.attachment_type.TEXT)
            allure.attach('Basket text', text_remove_product, allure.attachment_type.TEXT)
            assert alert_text == 'Success: You have added MacBook to your shopping cart!\n×'
            assert (
                text_remove_product
                == product_card_page.calculation_of_quantity_of_goods_in_basket(
                    data.check,
                    cost_of_product,
                )
            )
