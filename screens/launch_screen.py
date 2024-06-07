#Lancher BaseScreen - Andrew Stack 2024
from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen


class App(Enum):
    WEATHER = "WEATHER"
    GAMES = "GAMES"
    CARS = "CARS"
    BOOKS = "BOOKS"
    RECIPES = "RECIPES"
    LEARNING = "LEARNING"


class LaunchScreen(BaseScreen):
    screen_id = "SCREEN_LAUNCH"

    def launch_weather(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="WIDGET_WEATHER").click()

    def launch_app(self, app: App):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"APPBUTTON_{app.value}").click()
