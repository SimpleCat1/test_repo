from typing import TYPE_CHECKING, List

import allure
import pytest

from tests.main_page.search_input.parametrization_search import ParametrizationSearch
from tests.main_page.search_input.search_locators import SearchLocators
from tests.main_page.main_locators import MainLocators
from tests.main_page.search_input.search_page import SearchPage

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest


class TestSearchInput:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_product_search_input")
    @allure.description("checking the found search products")
    def test_product_search_input(
            self,
            request: 'FixtureRequest',
            search_page: 'SearchPage',
    ):
        search_page.open_url(request.config.getoption("--url"))
        with allure.step('Go to the registration page via the "My Account" drop-down list'):
            search_page.data_entry('MacBook', MainLocators.input_search)
            search_page.click(MainLocators.button_search)

        with allure.step('Data verification'):
            received_list_of_products: List[str] = [
                unit for unit in search_page.get_text_from_products(
                    SearchLocators.name_products,
                )
            ]
            allure.attach(
                ', '.join(received_list_of_products),
                'list of products received',
                allure.attachment_type.TEXT,
            )
            search_page.check_text_of_products('MacBook', received_list_of_products)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_empty_search_input")
    @allure.description("empty search")
    def test_empty_search_input(
            self,
            request: 'FixtureRequest',
            search_page: 'SearchPage',
    ):
        search_page.open_url(request.config.getoption("--url"))
        with allure.step('Go to the registration page via the "My Account" drop-down list'):
            search_page.data_entry('', MainLocators.input_search)
            search_page.click(MainLocators.button_search)

        with allure.step('Data verification'):
            search_page.element_invisibility(SearchLocators.card_products)
            header_search: str = search_page.get_text_element(
                SearchLocators.header_result_search,
            )
            allure.attach(
                header_search,
                'the search title looks like this',
                allure.attachment_type.TEXT,
            )
            assert header_search == 'Search'

    @pytest.mark.parametrize(
        "data",
        ParametrizationSearch.search_data,
        ids=[unit for unit in ParametrizationSearch.search_data],
    )
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_irrelevant_search_input")
    @allure.description("Irrelevant search for a product that does not exist")
    def test_irrelevant_search_input(
            self,
            request: 'FixtureRequest',
            search_page: 'SearchPage',
            data: str,
    ):
        search_page.open_url(request.config.getoption("--url"))
        with allure.step('Go to the registration page via the "My Account" drop-down list'):
            search_page.data_entry(data, MainLocators.input_search)
            search_page.click(MainLocators.button_search)

        with allure.step('Data verification'):
            search_page.element_invisibility(SearchLocators.card_products)
            header_search: str = search_page.get_text_element(
                SearchLocators.header_result_search,
            )
            allure.attach(
                header_search,
                'the search title looks like this',
                allure.attachment_type.TEXT,
            )
            assert header_search == f'Search - {data}'
