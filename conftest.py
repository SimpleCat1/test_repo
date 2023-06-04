from datetime import datetime
from typing import Generator, Any, Callable
import allure
import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest
from _pytest.python import Function
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.opera.webdriver import WebDriver
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from tests.main_page.main_page import MainPage


def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        '--url',
        type=str,
        action='store',
        default='http://192.168.0.100:8081',
        help="Choose url: https://www.schoolsw3.com or http://192.168.0.102:8081",
    )
    parser.addoption(
        '--browser',
        type=str,
        action='store',
        default='chrome',
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        '--remote',
        type=str,
        action='store',
        default='False',
        help="Choose remote: True or False",
    )
    parser.addoption(
        '--command_executor',
        type=str,
        action='store',
        default='http://192.168.0.100:4444/wd/hub',
        help="Choose remote url: http://192.168.0.102:4444/wd/hub or another",
    )
    parser.addoption(
        '--browser_version',
        type=str,
        action='store',
        default='80',
        help="Choose browser version: 80 or 81",
    )
    parser.addoption(
        '--browser_without_interfaces',
        type=str,
        action='store',
        default='false',
        help="Choose whether to display the browser: True or False",
    )


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Function) -> None:
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


# make a screenshot with a name of the test, date and time
def take_screenshot(driver: WebDriver, nodeid: str) -> None:
    file_name = (
        f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'
        .replace("/","_").replace("::","__")
    )
    allure.attach(
        driver.get_screenshot_as_png(),
        name=file_name,
        attachment_type=AttachmentType.PNG,
    )


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request: SubRequest) -> None:
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if all((
                request.node.rep_call.failed,
                True if len(
                    [True for _, unit in enumerate(request.node.fixturenames) if unit == 'browser']
                ) == 1 else False
        )):
            driver: WebDriver = request.node.funcargs['browser']
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)


@pytest.fixture(scope='session')
def choose_browser(request: SubRequest) -> Callable:
    def choose_browser() -> WebDriver:
        browser_choose: str = request.config.getoption("--browser")
        version: str = request.config.getoption("--browser_version")
        url_command_executor: str = request.config.getoption("--command_executor")
        remote_on: str = request.config.getoption("--remote")
        browser_interfaces: str = request.config.getoption("--browser_without_interfaces")
        browser_get: WebDriver
        caps = {
            "browserName": browser_choose,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": True,
                "screenResolution": "1280x720",
                "enableLog": True
            },
        }
        if browser_choose == 'firefox':
            from selenium.webdriver.firefox.options import Options

            if browser_interfaces == 'true' and remote_on == 'False':
                firefox_options = Options()
                firefox_options.add_argument("--disable-extensions")
                firefox_options.add_argument("--disable-gpu")
                firefox_options.add_argument("--no-sandbox")  # linux only
                firefox_options.add_argument("--headless")
                return webdriver.Firefox(GeckoDriverManager().install(), options=firefox_options)
            elif remote_on == 'False':
                return webdriver.Firefox(GeckoDriverManager().install())
            else:
                return webdriver.Remote(
                    command_executor=url_command_executor,
                    desired_capabilities=caps,
                )
        elif browser_choose == 'opera':
            from selenium.webdriver.opera.options import Options

            if browser_interfaces == 'true' and remote_on == 'False':
                opera_options = Options()
                opera_options.add_argument("--disable-extensions")
                opera_options.add_argument("--disable-gpu")
                opera_options.add_argument("--no-sandbox")  # linux only
                opera_options.add_argument("--headless")
                return webdriver.Opera(
                    options=opera_options,
                    executable_path=OperaDriverManager().install(),
                )
            elif remote_on == 'False':
                return webdriver.Opera(executable_path=OperaDriverManager().install())
            else:
                return webdriver.Remote(
                    command_executor=url_command_executor,
                    desired_capabilities=caps,
                )
        else:
            from selenium.webdriver.chrome.options import Options

            if browser_interfaces == 'true' and remote_on == 'False':
                chrome_options = Options()
                chrome_options.add_argument("--disable-extensions")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--no-sandbox")  # linux only
                chrome_options.add_argument("--headless")
                return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
            elif remote_on == 'False':
                return webdriver.Chrome(ChromeDriverManager().install())
            else:
                return webdriver.Remote(
                    command_executor=url_command_executor,
                    desired_capabilities=caps,
                )
    return choose_browser


@pytest.fixture(scope='session')
def browser(choose_browser: Callable) -> Generator[WebDriver, Any, None]:
    browser_get: WebDriver = choose_browser()
    browser_get.implicitly_wait(5)
    yield browser_get
    browser_get.close()


@pytest.fixture(scope='module')
def main_page(browser: WebDriver, request: SubRequest) -> MainPage:
    """
    Create a page class to get page methods.
    """
    def get_methods_page():
        return MainPage(browser, request)

    return get_methods_page()

