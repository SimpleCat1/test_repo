import logging
from typing import Union, Optional

import allure
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonHelperUi:

    logger: logging.Logger = None

    @allure.step("We are waiting for the element: {xpath} when it appears on the DOM html page")
    def element_visibility(
        self,
        driver: WebDriver,
        request: FixtureRequest,
        xpath: str,
    ) -> Optional[WebElement]:
        self._log_create(request)
        self.logger.info('Owe are waiting for the element to appear in the DOM of the Html page')
        element_found: Union[bool, WebElement] = (
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        )
        if element_found:
            driver.execute_script("return arguments[0].scrollIntoView(true);", element_found)
            self.logger.info(f'The element is visible: {xpath}')
            return element_found
        self.logger.critical(f'Element: {xpath} was not found')
        raise TimeoutError(f'Element: {xpath} was not found')

    @allure.step(
        "We are waiting for the element: {xpath} when it unappears on the page and DOM html page",
    )
    def element_invisibility(self, driver: WebDriver, request: FixtureRequest, xpath: str) -> None:
        self._log_create(request)
        self.logger.info('Owe are waiting for the element to appear in the DOM of the Html page')
        element_found: bool = (
            WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        )
        if not element_found:
            self.logger.critical(f'Element: {xpath} was not found')
            raise TimeoutError(f'Element: {xpath} was not found')
        self.logger.info(f'The element is invisibility: {xpath}')

    @allure.step("We expect that xpath: {xpath} will have this text: {text}")
    def text_to_be_present(
        self,
        driver: WebDriver,
        request: FixtureRequest,
        xpath: str,
        text: str,
    ) -> Union[bool, str]:
        self._log_create(request)
        self.logger.info('Owe are waiting for the element to appear in the DOM of the Html page')
        element_found: Union[bool, str] = (
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
                (By.XPATH, xpath), text),
            )
        )
        if element_found:
            driver.execute_script(
                "return arguments[0].scrollIntoView(true);",
                driver.find_element_by_xpath(xpath),
            )
            self.logger.info(f'The element is visible: {xpath}')
            return element_found
        self.logger.critical(f'Element: {xpath} was not found')
        raise TimeoutError(f'Element: {xpath} was not found')

    @allure.step("Click on the element xpath: {xpath} or web_element: {web_element}")
    def click(
        self,
        browser: WebDriver,
        request: FixtureRequest,
        xpath: str = None,
        web_element: WebElement = None,
    ) -> None:
        self._log_create(request)
        if web_element:
            web_element.click()
            self.logger.info(f'I click on the Element: {web_element}')
        else:
            browser.find_element_by_xpath(xpath).click()
            self.logger.info(f'I click on the Element: {xpath}')

    @allure.step("Opening the site by url: {url}")
    def open_url(self, browser: WebDriver, request: FixtureRequest, url: str = None) -> None:
        self._log_create(request)
        browser.get(url)
        self.logger.info(f'Open the url: {url}')

    @allure.step("Getting the text from the element xpath: {xpath} or web_element: {web_element}")
    def get_text_element(
            self,
            browser: WebDriver,
            request: FixtureRequest,
            xpath: str = None,
            web_element: WebElement = None,
    ) -> str:
        self._log_create(request)
        if web_element:
            self.logger.info(f'got the text from the element: {web_element.text}')
            return web_element.text
        else:
            self.logger.info(
                f'got the text from the element: {browser.find_element_by_xpath(xpath).text}',
            )
            return browser.find_element_by_xpath(xpath).text

    @allure.step(
        "Sending the text {value} to the element xpath: {xpath} or web_element: {web_element}",
    )
    def data_entry(
            self,
            browser: WebDriver,
            request: FixtureRequest,
            value: str,
            xpath: str = None,
            web_element: WebElement = None,
    ) -> None:
        self._log_create(request)
        if web_element:
            self.logger.info(f'sent the text to the element: {value}')
            web_element.send_keys(value)
        else:
            self.logger.info(f'sent the text to the element: {value}')
            browser.find_element_by_xpath(xpath).send_keys(value)

    def _log_create(self, request: FixtureRequest) -> None:
        """
        Create an action step in a .log file, with the date and logging level.

        If the file exists, it will overwrite it.
        """
        if self.logger is None:
            self.logger = logging.getLogger(request.node.name)
            file_handler = logging.FileHandler(f"{request.node.name}.log", 'w+', 'utf-8')
            file_handler.setFormatter(
                logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
            )
            self.logger.addHandler(file_handler)
            self.logger.setLevel(level="DEBUG")
