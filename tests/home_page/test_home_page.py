from typing import TYPE_CHECKING

import allure

from tests.common_helper_ui import CommonHelperUi
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from _pytest.fixtures import FixtureRequest


class TestHomePage(CommonHelperUi):

    def test_home_page(self, browser: 'WebDriver', request: 'FixtureRequest'):
        self.open_url(browser, request, request.config.getoption("--url"))

        with allure.step('Data verification'):
            self.logger.info(f"got the text from the element: {browser.title}")
            allure.attach(
                'Title page',
                browser.title,
                allure.attachment_type.TEXT,
            )
            assert browser.title == 'Your Store'
