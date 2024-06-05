#Lancher BaseScreen - Andrew Stack 2024

from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen


class LaunchScreen(BaseScreen):
    screen_id = "SCREEN_LAUNCH"

    def go_to_weather_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="WIDGET_WEATHER").click()

    def go_to_games_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_GAMES").click()

    def go_to_cars_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_CARS").click()

    def go_to_books_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_BOOKS").click()

    def go_to_recipes_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_RECIPES").click()

    def go_to_learning_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_LEARNING").click()

    def go_to_map_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_MAP").click()

    def go_to_tdarr_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_TDARR").click()

    def go_to_plex_dash_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_PLEX_DASH").click()

    def go_to_requests_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_REQUESTS").click()

    def go_to_pihole_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_PIHOLE").click()

    def go_to_homebridge_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_HOMEBRIDGE").click()

    def go_to_stackk_me_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_STACKK.ME").click()

    def go_to_storage_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_STORAGE").click()

    def go_to_browser_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_BROWSER").click()

    def go_to_settings_screen(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_SETTINGS").click()
