from enum import Enum

from selenium.common import NoSuchElementException

from screens.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy

class Game(Enum):
    SLOTS = "SLOTS"
    WAR = "WAR"
    DICE_WAR = "DICEWAR"
    DICE_ROLLER = "DICEROLLER"
    CARD_FLIPPER = "CARDFLIPPER"
    SETTING = "SETTINGS"

class GamesScreen(BaseScreen):
    screen_id = "SCREEN_GAMES"

    def go_to_game(self, game: Game):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"APPBUTTON_{game.value}").click()

    def is_on_game(self, game: Game) -> bool:
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"SCREEN_GAMES_{game.value}")
            return True
        except NoSuchElementException:
            return False

