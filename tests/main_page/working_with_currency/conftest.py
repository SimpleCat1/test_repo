import allure
import pytest


@pytest.fixture
def return_default_currency_settings(browser, main_page) -> None:
    """
    Return the currency to the default value.
    """
    yield
    with allure.step('We return the currency settings to default'):
        main_page.changing_currency('USD')
