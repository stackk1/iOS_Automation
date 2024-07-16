import re
from appium.webdriver.common.appiumby import AppiumBy


class ValueChecker:
    def __init__(self, driver):
        self.driver = driver

    def get_value(self, accessibility_id):
        element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=accessibility_id)
        score_text = element.text
        score = re.sub("[^0-9]", "", score_text)
        print(f"score = {score}")
        return int(score) if score else 0
