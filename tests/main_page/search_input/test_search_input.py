from typing import TYPE_CHECKING, List

import allure
import pytest

from tests.main_page.search_input.parametrization_search import ParametrizationSearch
from tests.main_page.search_input.search_page_locators import SearchPageLocators
from tests.main_page.main_page_locators import MainPageLocators
from tests.main_page.search_input.search_page import SearchPage

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest
    from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.mark.usefixtures("search_page")
class TestSearchInput:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_admin_login_page")
    @allure.description("The Login page is displayed when navigating through the tab")
    def test_product_search_input(
            self,
            browser: 'WebDriver',
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
            SearchPage.check_text_of_products('MacBook', received_list_of_products)
            allure.attach(
                'list of products received',
                received_list_of_products,
                allure.attachment_type.TEXT,
            )

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_admin_login_page")
    @allure.description("The Login page is displayed when navigating through the tab")
    def test_empty_search_input(
            self,
            browser: 'WebDriver',
            request: 'FixtureRequest',
            search_page: 'SearchPage',
    ):
        search_page.open_url(request.config.getoption("--url"))
        with allure.step('Go to the registration page via the "My Account" drop-down list'):
            search_page.data_entry('', MainPageLocators.input_search)
            search_page.click(MainPageLocators.button_search)

        with allure.step('Data verification'):
            search_page.element_invisibility(SearchPageLocators.card_products)
            search_page.text_to_be_present(SearchPageLocators.header_result_search, 'Search')
            allure.attach(
                'the search title looks like this',
                'Search',
                allure.attachment_type.TEXT,
            )

    @pytest.mark.parametrize(
        "data",
        ParametrizationSearch.search_data,
        ids=[unit for unit in ParametrizationSearch.search_data],
    )
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_admin_login_page")
    @allure.description("The Login page is displayed when navigating through the tab")
    def test_irrelevant_search_input(
            self,
            browser: 'WebDriver',
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
            search_page.text_to_be_present(
                SearchPageLocators.header_result_search,
                f'Search - {data}',
            )
            allure.attach(
                'the search title looks like this',
                f'Search - {data}',
                allure.attachment_type.TEXT,
            )
