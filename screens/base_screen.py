#BaseScreen Driver - Andrew Stack 2024

from abc import ABC
from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException


class BaseScreen(ABC):
    screen_id: str
    driver: webdriver

    def __init__(self):
        if not self.screen_id:
            raise Exception("missing screen_id")
        if not self.is_here():
            raise Exception(f"Driver was not at {self.__class__.__name__} - {self.screen_id}")

    def is_here(self) -> bool:
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=self.screen_id)
            return True
        except NoSuchElementException:
            return False
