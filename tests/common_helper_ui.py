import logging
import time
from typing import Union, Optional

import allure
from _pytest.fixtures import FixtureRequest
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonHelperUi:

    logger: logging.Logger = None

    def __init__(self, driver: WebDriver, request: FixtureRequest):
        self.driver = driver
        self.request = request

    @allure.step("We are waiting for the element: {xpath} when it appears on the DOM html page")
    def element_visibility(self, xpath: str) -> Optional[WebElement]:
        self._log_create()
        self.logger.info('Owe are waiting for the element to appear in the DOM of the Html page')
        element_found: Union[bool, WebElement] = (
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((
                By.XPATH,
                xpath,
            )))
        )
        if element_found:
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", element_found)
            self.logger.info(f'The element is visible: {xpath}')
            return element_found
        self.logger.critical(f'Element: {xpath} was not found')
        raise TimeoutError(f'Element: {xpath} was not found')

    @allure.step(
        "We are waiting for the element: {xpath}"
        " when it appears on the DOM html page (may be invisible)",
    )
    def element_presence_in_dom(self, xpath: str) -> WebElement:
        self._log_create()
        self.logger.info('Owe are waiting for the element to appear in the DOM of the Html page')
        try:
            element_found: WebElement = (
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                    By.XPATH,
                    xpath,
                )))
            )
            self.logger.info(f'The element is presence: {xpath}')
            return element_found
        except NoSuchElementException as es:
            self.logger.critical(f'Element: {xpath} was not found')
            raise es

    @allure.step(
        "We are waiting for the element: {xpath} when it unappears on the page and DOM html page",
    )
    def element_invisibility(self, xpath: str) -> None:
        self._log_create()
        self.logger.info('Owe are waiting for the element to appear in the DOM of the Html page')
        element_found: bool = (
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((
                By.XPATH,
                xpath,
            )))
        )
        if not element_found:
            self.logger.critical(f'Element: {xpath} was not found')
            raise TimeoutError(f'Element: {xpath} was not found')
        self.logger.info(f'The element is invisibility: {xpath}')

    @allure.step("We expect that xpath: {xpath} will have this text: {text}")
    def text_to_be_present(self, xpath: str, text: str) -> bool:
        self._log_create()
        self.logger.info('Owe are waiting for the element to appear in the DOM of the Html page')
        element_found: bool = (
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
                (By.XPATH, xpath), text),
            )
        )
        if element_found:
            self.driver.execute_script(
                "return arguments[0].scrollIntoView(true);",
                self.driver.find_element_by_xpath(xpath),
            )
            self.logger.info(f'The element is visible: {xpath}')
            return element_found
        self.logger.critical(f'Element: {xpath} was not found')
        raise TimeoutError(f'Element: {xpath} was not found')

    @allure.step("Click on the element xpath: {xpath}")
    def click(self, xpath: str = None, explicit_expectation_method: str = None) -> None:
        """
        The method is intended both for normal pressing and for calling an explicit element waiting
        """
        self._log_create()
        if explicit_expectation_method:
            self.__getattribute__(explicit_expectation_method)(xpath).click()
        else:
            self.driver.find_element_by_xpath(xpath).click()
        self.logger.info(f'I click on the Element: {xpath}')

    @allure.step("Opening the site by url: {url}")
    def open_url(self, url: str = None) -> None:
        self._log_create()
        self.driver.get(url)
        self.logger.info(f'Open the url: {url}')

    @allure.step("Getting the text from the element xpath: {xpath}")
    def get_text_element(self, xpath: str = None, explicit_expectation_method: str = None) -> str:
        """
        The method is intended both for the usual receipt of text,
         and for calling an explicit expectation of an element.
        """
        def _attempts_to_get_text() -> str:
            """
            Work around the StaleElementReferenceException error.
            """
            for _ in range(1, 3):
                try:
                    return self.__getattribute__(explicit_expectation_method)(xpath).text
                except StaleElementReferenceException:
                    self.logger.info(
                        'we are trying to make a request again, ChromeDriver(BrowserDriver),'
                        ' to give a new locator'
                    )
        self._log_create()
        if explicit_expectation_method:
            text = _attempts_to_get_text()
            self.logger.info(f'got the text from the element: {text}')
            return text
        else:
            self.logger.info(
                f'got the text from the element: {self.driver.find_element_by_xpath(xpath).text}',
            )
            return self.driver.find_element_by_xpath(xpath).text

    @allure.step(
        "Sending the text {value} to the element xpath: {xpath}",
    )
    def data_entry(
            self,
            value: str,
            xpath: str = None,
            explicit_expectation_method: str = None,
    ) -> None:
        """
        The method is intended both for normal input and for calling an explicit element wait
        """
        self._log_create()
        if explicit_expectation_method:
            web_element: WebElement = self.__getattribute__(explicit_expectation_method)(xpath)
            web_element.clear()
            web_element.send_keys(value)
        else:
            self.driver.find_element_by_xpath(xpath).send_keys(value)
        self.logger.info(f'sent the text to the element: {value}')

    def _log_create(self) -> None:
        """
        Create an action step in a .log file, with the date and logging level.

        If the file exists, it will overwrite it.
        """
        if self.logger is None:
            self.logger = logging.getLogger(self.request.node.name)
            file_handler = logging.FileHandler(f"{self.request.node.name}.log", 'w+', 'utf-8')
            file_handler.setFormatter(
                logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
            )
            self.logger.addHandler(file_handler)
            self.logger.setLevel(level="DEBUG")
