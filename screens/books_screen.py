from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from screens.base_screen import BaseScreen


class Book(Enum):
    AMAZING_WORDS = "Amazing Words"
    L_F_R = "Literature For Reading"
    TEXT_AND_MORE = "Text and More"
    C_W_P = "Characters, Words, and Paragraphs"
    A_B_IT = "A Book, I Think"


class BooksScreen(BaseScreen):
    screen_id = "SCREEN_BOOKS"

    def open_book(self, book: str):
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"BOOK_{book}").click
        except NoSuchElementException:
            max_scrolls = 5
            for _ in range(max_scrolls):
                self.scroll_down()
                try:
                    self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"BOOK_{book}").click()
                    return
                except NoSuchElementException:
                    continue
            print(f"No book with title {book}")

    def is_on_book(self, book: str) -> bool:
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"BOOK_{book}")
            return True
        except:
            print(f"{book} failed to open")
            return False
