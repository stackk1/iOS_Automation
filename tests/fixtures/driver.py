#driver fixture - Andrew Stack 2024
import os
from typing import Dict

import pytest
from _pytest.fixtures import SubRequest
from _pytest.reports import CollectReport
from _pytest.stash import StashKey
from appium.options.ios import XCUITestOptions
from appium import webdriver
from screens.base_screen import BaseScreen

APP_PATH = os.environ["APP_PATH"]

# https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
phase_report_key = StashKey[Dict[str, CollectReport]]()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call) -> None:
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # store test results for each phase of a call, which can
    # be "setup", "call", "teardown"
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep

@pytest.fixture(autouse=True)
def driver(request):
    options = XCUITestOptions().load_capabilities({
        'platformVersion': '17.5',
        'app': APP_PATH,
        'deviceName': "iPhone 15"
    })
    driver = webdriver.Remote(
        # Appium1 points to http://127.0.0.1:4723/wd/hub by default
        'http://127.0.0.1:4723',
        options=options,
        direct_connection=True
    )
    BaseScreen.driver = driver
    yield
    report = request.node.stash[phase_report_key]
    if report["call"].failed:
        print(driver.page_source)
