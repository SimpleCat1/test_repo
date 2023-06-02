from typing import TYPE_CHECKING
import allure
import pytest

from tests.main_page.main_page_locators import MainPageLocators

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest
    from tests.main_page.main_page import MainPage


class TestChangCurrency:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("test_change_currency")
    @allure.description("The currency changes on the main page")
    @pytest.mark.unparalleled
    def test_change_currency(
            self,
            request: 'FixtureRequest',
            main_page: 'MainPage',
            return_default_currency_settings: 'None',
    ):
        main_page.open_url(request.config.getoption("--url"))
        with allure.step('Changed the currency on the main page'):
            main_page.changing_currency('EUR')

        with allure.step('Data verification'):
            text_currency: str = main_page.get_text_element(MainPageLocators.currency_value)
            allure.attach('Text currency', text_currency, allure.attachment_type.TEXT)
            assert text_currency == '€'
