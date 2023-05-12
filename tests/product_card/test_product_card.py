from typing import TYPE_CHECKING

import allure

from tests.common_helper_ui import CommonHelperUi
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from _pytest.fixtures import FixtureRequest


class TestProductCard(CommonHelperUi):

    def test_product_card(self, browser: 'WebDriver', request: 'FixtureRequest'):
        self.open_url(browser, request, request.config.getoption("--url"))
        with allure.step('Clicked on the product'):
            self.click(
                browser,
                request,
                "//div[contains(@class,'product-thumb')]//img[position()=1]",
                'element_visibility',
            )

        with allure.step('Data verification'):
            name_product: str = self.get_text_element(
                browser,
                request,
                "//div[@class='col-sm-4']/h1",
            )
            allure.attach(
                'Name product',
                name_product,
                allure.attachment_type.TEXT,
            )
            assert name_product == 'MacBook'
