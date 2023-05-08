from datetime import datetime
from typing import Generator, Any

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


def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        '--url',
        type=str,
        action='store',
        default='http://192.168.0.102:8081',
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
        default='http://192.168.0.102:4444/wd/hub',
        help="Choose remote url: http://192.168.0.102:8080/wd/hub or another",
    )
    parser.addoption(
        '--browser_version',
        type=str,
        action='store',
        default='80',
        help="Choose browser version: 80 or 81",
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
def browser(request: SubRequest) -> Generator[WebDriver, Any, None]:
    browser_choose: str = request.config.getoption("--browser")
    version: str = request.config.getoption("--browser_version")
    url_command_executor: str = request.config.getoption("--command_executor")
    remote_on: bool = request.config.getoption("--remote")
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
        browser_get = (
            webdriver.Remote(
                command_executor=url_command_executor,
                desired_capabilities={"browserName": browser_choose},
            ) if remote_on == 'True' else webdriver.Firefox()
        )
    elif browser_choose == 'opera':
        browser_get = (
            webdriver.Remote(
                command_executor=url_command_executor,
                desired_capabilities={"browserName": browser_choose},
            ) if remote_on == 'True' else webdriver.Opera()
        )
    else:
        browser_get = (
            webdriver.Remote(
                command_executor=url_command_executor,
                desired_capabilities=caps,
            ) if remote_on == 'True' else webdriver.Chrome()
        )
    browser_get.implicitly_wait(5)
    yield browser_get
    browser_get.close()
