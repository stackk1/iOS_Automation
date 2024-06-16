from enum import Enum

from selenium.common import NoSuchElementException

from screens.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy


class Game(Enum):
    SLOTS = "SLOTS"
    WAR = "WAR"
    DICE_WAR = "DICE_WAR"
    DICE_ROLLER = "DICE_ROLLER"
    CARD_FLIPPER = "CARD_FLIPPER"


class GamesScreen(BaseScreen):
    screen_id = "SCREEN_GAMES"

    def go_to_game(self, game: str):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"APPBUTTON_{game}").click()
        print(f"clicking APPBUTTON_{game}")

    def is_on_game(self, game: str) -> bool:
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"SCREEN_GAMES_{game}")
            return True
        except NoSuchElementException:
            print(f"Did not find SCREEN_GAMES_{game}")
            return False

    def go_to_settings(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SETTINGSBUTTON_GAMES").click()

    def is_on_game_settings(self):
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SCREEN_GAMES_SETTINGS")
            return True
        except NoSuchElementException:
            return False

    def get_slot_score(self):
        slot_score = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="VIEW_SCORE_VALUE")
        return slot_score

    def press_button(self, button: str):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"BUTTON_{button}").click()