#Lancher BaseScreen - Andrew Stack 2024

from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen


class LaunchScreen(BaseScreen):
    screen_id = "SCREEN_LAUNCH"

    def go_to_weather_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="WIDGET_WEATHER").click()
