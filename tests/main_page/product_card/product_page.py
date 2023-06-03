from typing import Union

from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver

from tests.main_page.main_page import MainPage
from tests.main_page.product_card.product_page_locators import ProductPageLocators


class ProductPage(MainPage):

    def __init__(self, driver: WebDriver, request: FixtureRequest):
        super().__init__(driver, request)

    def open_url_card_page(self, name_product: str) -> None:
        url_for_open = ''.join((self.request.config.getoption("--url"), '/', name_product))
        if self.driver.current_url != url_for_open:
            self.open_url(url_for_open)

    def calculation_of_quantity_of_goods_in_basket(
            self,
            count_product: Union[str, int],
            cost_product: float,
    ) -> str:
        result_calculation_cost: float = round(cost_product * float(count_product), 2)
        if len(str(result_calculation_cost).split('.')[1]) == 2:

            return ''.join((
                str(count_product), ' item(s) - $',
                str("{:,.2f}".format(result_calculation_cost)),
            ))
        else:
            return ''.join((
                str(count_product),
                ' item(s) - $',
                str("{:,.2f}".format(result_calculation_cost)),
            ))

    def adding_quantity_of_product(self, data: Union[str, int, float]) -> float:
        """
        Adding the quantity of the product to the Input of the product card.
        """
        self.driver.find_element_by_xpath(
            ProductPageLocators.input_count_product,
        ).clear()
        self.data_entry(data, ProductPageLocators.input_count_product)
        self.click(ProductPageLocators.button_add_count_product)
        return float(self.get_text_element(
            ProductPageLocators.text_cost_of_product,
        ).replace('$', ''))
