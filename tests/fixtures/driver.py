#driver fixture - Andrew Stack 2024

import pytest
import os
from appium.options.ios import XCUITestOptions
from appium import webdriver

from screens.base_screen import BaseScreen

#APP_PATH = os.environ.get("APP_PATH")

@pytest.fixture(autouse=True)
def driver():
    options = XCUITestOptions().load_capabilities({
        'platformVersion': '17.5',
        'app': '/Users/andrew/Library/Developer/Xcode/DerivedData/X-clqytwwdyrqhzkayaqjbboneizhx/Build/Products/Debug-iphonesimulator/X.app',
        'deviceName': "iPhone 15"
    })
    driver = webdriver.Remote(
        # Appium1 points to http://127.0.0.1:4723/wd/hub by default
        'http://127.0.0.1:4723',
        options=options,
        direct_connection=True
    )
    BaseScreen.driver = driver
