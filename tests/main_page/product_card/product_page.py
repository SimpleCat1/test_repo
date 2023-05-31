from typing import Union

from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver

from tests.main_page.main_page import MainPage


class ProductPage(MainPage):


    def __init__(self, driver: WebDriver, request: FixtureRequest):
        super().__init__(driver, request)

    def open_url_card_page(self, name_product: str) -> None:
        url_for_open = ''.join((self.request.config.getoption("--url"), '/', name_product))
        if self.driver.current_url != url_for_open:
            self.open_url(url_for_open)

    def calculation_of_quantity_of_goods_in_basket(self, count_product: Union[str, int], cost_product: float) -> str:
        result_calculation_cost: float = round(cost_product * float(count_product), 2)
        if len(str(result_calculation_cost).split('.')[1]) == 2:

            return ''.join((str(count_product), ' item(s) - $', str("{:,.2f}".format(result_calculation_cost))))
        else:
            return ''.join((
                str(count_product),
                ' item(s) - $',
                str("{:,.2f}".format(result_calculation_cost)),
            ))
