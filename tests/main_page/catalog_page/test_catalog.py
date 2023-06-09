from typing import TYPE_CHECKING

import allure
import pytest

from tests.main_page.catalog_page.catalog_locators import CatalogLocators
from tests.main_page.catalog_page.parametrization_catalog import ParametrizationCatalog

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest
    from tests.main_page.main_page import MainPage


class TestCatalog:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_component_tab_breadcrumb")
    @allure.description("Page 'Monitor' bread crumbs")
    def test_component_tab_breadcrumb(
            self,
            request: 'FixtureRequest',
            main_page: 'MainPage',
    ):
        main_page.open_url(request.config.getoption("--url"))
        with allure.step('Selecting an item from the Components tab'):
            main_page.click(main_page.components_tab, 'element_visibility')
            main_page.click(main_page.components_tab_monitors, 'element_visibility')

        with allure.step('Data verification'):
            assert (
                    main_page.get_text_element(CatalogLocators.breadcrumb_last_elements)
                    == 'Monitors'
            )
            main_page.logger.info(
                "So many elements have been found: "
                f"{len(main_page.driver.find_elements_by_xpath(CatalogLocators.breadcrumb))}"
            )
            allure.attach(
                str(len(main_page.driver.find_elements_by_xpath(CatalogLocators.breadcrumb))),
                'Number of elements in bread crumbs',
                allure.attachment_type.TEXT,
            )
            assert len(main_page.driver.find_elements_by_xpath(CatalogLocators.breadcrumb)) == 3

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_return_to_main_page_with_empty_directory")
    @allure.description(
        "return to the main page via the button if there is no product in the catalog"
        " (the 'mice_and_trackballs' tab)",
    )
    def test_return_to_main_page_with_empty_directory(
            self,
            request: 'FixtureRequest',
            main_page: 'MainPage',
    ):
        main_page.open_url(request.config.getoption("--url"))
        with allure.step('Selecting an item from the Components tab'):
            main_page.click(main_page.components_tab, 'element_visibility')
            main_page.click(main_page.components_tab_mice_and_trackballs, 'element_visibility')
            main_page.click(CatalogLocators.button_continue, 'element_visibility')

        with allure.step('Data verification'):
            current_url: str = main_page.driver.current_url
            allure.attach(current_url, 'browser url', allure.attachment_type.TEXT)
            assert (
                current_url
                == ''.join((request.config.getoption("--url"), '/index.php?route=common/home'))
            )

    @pytest.mark.parametrize(
        "data",
        ParametrizationCatalog.search_data,
        ids=[unit.name for unit in ParametrizationCatalog.search_data],
    )
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_mice_and_trackballs_title")
    @allure.description(
        "The 'Mice and Trackballs' product page is displayed when clicking on the 'Components' tab."
        " Checking the header",
    )
    def test_mice_and_trackballs_title(
            self,
            request: 'FixtureRequest',
            main_page: 'MainPage',
            data: 'data_tuple',
    ):
        main_page.open_url(request.config.getoption("--url"))
        with allure.step('Selecting an item from the Components tab'):
            main_page.click(main_page.components_tab, 'element_visibility')
            main_page.click(
                main_page.components_tab.replace("']", ''.join((data.url, "']"))),
                'element_visibility',
            )

        with allure.step('Data verification'):
            catalog_title: str = main_page.get_text_element(CatalogLocators.header_catalog)
            allure.attach(catalog_title, 'catalog title', allure.attachment_type.TEXT)
            assert catalog_title == data.name
