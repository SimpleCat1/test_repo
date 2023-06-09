import re
from typing import Generator, Any, List

import allure
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver

from tests.main_page.main_page import MainPage


class SearchPage(MainPage):

    def __init__(self, driver: WebDriver, request: FixtureRequest):
        super().__init__(driver, request)

    @allure.step('Getting the product search result')
    def get_text_from_products(self, xpath: str) -> Generator[Any, Any, None]:
        """
        We get a list of found products.
        """
        self.logger.info('Getting the product search result.')
        return (unit_element.text for unit_element in self.driver.find_elements_by_xpath(xpath))

    @allure.step(
        "We check that the list is relevant to the search query."
        " text_check: {text_check}, compare with: {data}",
    )
    def check_text_of_products(self, text_check: str, data: List[str]) -> None:
        """
        We check that the list is relevant to the search query.
        """
        self.logger.info(
            'We check that the list is relevant to the search query. '
            f'text_check: {text_check}, compare with: {data}',
        )
        for check in (re.match(text_check, unit) is not None for unit in data):
            assert check is not False
