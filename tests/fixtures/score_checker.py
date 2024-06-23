import re
from appium.webdriver.common.appiumby import AppiumBy


class ScoreChecker:
    def __init__(self, driver):
        self.driver = driver

    def get_score(self, accessibility_id):
        element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=accessibility_id)
        score_text = element.text
        score = re.sub("[^0-9]", "", score_text)
        return int(score) if score else 0
