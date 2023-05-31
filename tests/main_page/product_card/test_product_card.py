from typing import TYPE_CHECKING

import allure
import pytest

from tests.main_page.main_page_locators import MainPageLocators
from tests.main_page.product_card.parametrization_card_product import ParametrizationCardProduct
from tests.main_page.product_card.product_page_locators import ProductPageLocators

if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from _pytest.fixtures import FixtureRequest
    from tests.main_page.main_page import MainPage


@pytest.mark.usefixtures("main_page", "product_card_page")
class TestProductCard:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_product_card")
    @allure.description("The title of the product catalog is displayed")
    def test_product_card(self, browser: 'WebDriver', request: 'FixtureRequest', main_page: 'MainPage'):
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
    @allure.title("test_product_card")
    @allure.description("The title of the product catalog is displayed")
    def test_product_card(self, browser: 'WebDriver', product_card_page: 'ProductPage', data: 'data_tuple',
            return_default_bucket_state: 'None'):
        product_card_page.open_url_card_page('macbook')

        with allure.step('Data verification'):
            product_card_page.driver.find_element_by_xpath(ProductPageLocators.input_count_product).clear()
            product_card_page.data_entry(data.count_product, ProductPageLocators.input_count_product)
            product_card_page.click(ProductPageLocators.button_add_count_product)
            cost_of_product = float(product_card_page.get_text_element(ProductPageLocators.text_cost_of_product).replace('$',''))

        with allure.step('Data verification'):
            alert_text = product_card_page.get_text_element(MainPageLocators.alert, 'element_visibility')
            text_remove_product = product_card_page.get_text_element(
                MainPageLocators.basket,
                'element_visibility',
            )
            allure.attach('Alert text', alert_text, allure.attachment_type.TEXT)
            allure.attach('Basket text', text_remove_product, allure.attachment_type.TEXT)
            assert alert_text == 'Success: You have added MacBook to your shopping cart!\n×'
            assert text_remove_product == product_card_page.calculation_of_quantity_of_goods_in_basket(data.check, cost_of_product)
