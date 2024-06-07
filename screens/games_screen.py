from selenium.common import NoSuchElementException

from screens.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy


class GamesScreen(BaseScreen):
    screen_id = "SCREEN_GAMES"

    def go_to_slots(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="APPBUTTON_SLOTS").click()

    def is_on_slots_screen(self) -> bool:
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SCREEN_GAMES_SLOTS")
            return True
        except NoSuchElementException:
            return False
