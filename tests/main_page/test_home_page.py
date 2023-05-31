from typing import TYPE_CHECKING

import allure
import pytest

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest
    from tests.main_page.main_page import MainPage


@pytest.mark.usefixtures("main_page")
class TestHomePage:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_home_page")
    @allure.description("The title page of the main page is displayed correctly")
    def test_title_main_page(self, request: 'FixtureRequest', main_page: 'MainPage'):
        main_page.open_url(request.config.getoption("--url"))

        with allure.step('Data verification'):
            main_page.logger.info(f"got the text from the element: {main_page.driver.title}")
            allure.attach('Title page', main_page.driver.title, allure.attachment_type.TEXT)
            assert main_page.driver.title == 'Your Store'
