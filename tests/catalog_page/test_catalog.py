from typing import TYPE_CHECKING

import allure

from tests.common_locators import CommonLocators
from tests.common_helper_ui import CommonHelperUi
if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from _pytest.fixtures import FixtureRequest


class TestCatalog(CommonHelperUi):

    def test_catalog(self, browser: 'WebDriver', request: 'FixtureRequest'):
        self.open_url(browser, request, request.config.getoption("--url"))
        self.click(
            browser,
            request,
            web_element=self.element_visibility(
                browser,
                request,
                ''.join(("//li/a[@href='", request.config.getoption("--url"), "/component']")),
            ),
        )
        self.click(
            browser,
            request,
            web_element=self.element_visibility(
                browser,
                request,
                ''.join(("//a[@href='", request.config.getoption("--url"), "/component/monitor']")),
            ),
        )

        with allure.step('Data verification'):
            assert (
                self.get_text_element(browser, request, f"{CommonLocators.breadcrumb}[last()]/a")
                == 'Monitors'
            )
            self.logger.info(
                "So many elements have been found: "
                f"{len(browser.find_elements_by_xpath(CommonLocators.breadcrumb))}"
            )
            allure.attach(
                'Number of elements in bread crumbs',
                len(browser.find_elements_by_xpath(CommonLocators.breadcrumb)),
                allure.attachment_type.TEXT,
            )
            assert len(browser.find_elements_by_xpath(CommonLocators.breadcrumb)) == 3
