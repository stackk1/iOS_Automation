import re
from enum import Enum

from selenium.common import NoSuchElementException
from screens.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy

from tests.fixtures.score_checker import ScoreChecker


class Game(Enum):
    SLOTS = "SLOTS"
    WAR = "WAR"
    DICE_WAR = "DICE_WAR"
    DICE_ROLLER = "DICE_ROLLER"
    CARD_FLIPPER = "CARD_FLIPPER"


class GamesScreen(BaseScreen):
    screen_id = "SCREEN_GAMES"

    def go_to_game(self, game: str):
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"APPBUTTON_{game}").click()
        except:
            print(f"Failed to click APPBUTTON_{game}")

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
            print("Did not find Settings")
            return False

    def press_button(self, button: str):
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"BUTTON_{button}").click()
        except:
            print(f"BUTTON_{button} not found")
            return False

    def get_slot_score(self) -> int:
        slot_score_value = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SLOT_SCORE_VALUE")
        score = re.sub("[^0-9]", "",
                       slot_score_value.text)
        return int(score)

    def get_war_cards_remaining(self) -> int:
        war_cards_remaining = ScoreChecker.get_score(self,"WAR_CARDS_REMAINING_VALUE")
        return war_cards_remaining

    def get_dice_war_score(self):
        player_score = ScoreChecker.get_score(self,"PLAYER_SCORE_VALUE")
        cpu_score = ScoreChecker.get_score(self,"CPU_SCORE_VALUE")
        tie_score = ScoreChecker.get_score(self,"TIE_SCORE_VALUE")
        dice_score = player_score + cpu_score + tie_score
        return dice_score

    def get_dice_roller_count(self):
        count = ScoreChecker.get_score(self, "DICE_TOTAL_VALUE")
        return count

    def get_card_flipper_value(self):
        card_value = ScoreChecker.get_score(self, "CARD_VALUE")
        return card_value