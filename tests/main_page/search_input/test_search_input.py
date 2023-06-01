from typing import TYPE_CHECKING, List

import allure
import pytest

from tests.main_page.search_input.parametrization_search import ParametrizationSearch
from tests.main_page.search_input.search_page_locators import SearchPageLocators
from tests.main_page.main_page_locators import MainPageLocators
from tests.main_page.search_input.search_page import SearchPage

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest


@pytest.mark.usefixtures("search_page")
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
            search_page.data_entry('MacBook', MainPageLocators.input_search)
            search_page.click(MainPageLocators.button_search)

        with allure.step('Data verification'):
            received_list_of_products: List[str] = [
                unit for unit in search_page.get_text_from_products(
                    SearchPageLocators.name_products,
                )
            ]
            allure.attach(
                'list of products received',
                received_list_of_products,
                allure.attachment_type.TEXT,
            )
            SearchPage.check_text_of_products('MacBook', received_list_of_products)

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
            search_page.data_entry('', MainPageLocators.input_search)
            search_page.click(MainPageLocators.button_search)

        with allure.step('Data verification'):
            search_page.element_invisibility(SearchPageLocators.card_products)
            header_search: str = search_page.get_text_element(
                SearchPageLocators.header_result_search,
            )
            allure.attach(
                'the search title looks like this',
                header_search,
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
            search_page.data_entry(data, MainPageLocators.input_search)
            search_page.click(MainPageLocators.button_search)

        with allure.step('Data verification'):
            search_page.element_invisibility(SearchPageLocators.card_products)
            header_search: str = search_page.get_text_element(
                SearchPageLocators.header_result_search,
            )
            allure.attach(
                'the search title looks like this',
                header_search,
                allure.attachment_type.TEXT,
            )
            assert header_search == f'Search - {data}'
