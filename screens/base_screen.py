#BaseScreen Driver - Andrew Stack 2024

from abc import ABC
from random import random

from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys


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

    def swipe(self, start_x, start_y, end_x, end_y):
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def input_text(self, field_id, text: str):
        try:
            text_box = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"TEXTINPUT_{field_id}")
            text_box.send_keys(text + Keys.ENTER)
        except NoSuchElementException:
            print(f"No element with name TEXTINPUT_{field_id}")

    def get_text(self, field_id):
        try:
            text_box = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"TEXTINPUT_{field_id}")
            box_text = text_box.get_attribute("value")
            return box_text
        except NoSuchElementException:
            print(f"No element with name TEXTINPUT_{field_id}")