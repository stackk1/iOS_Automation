from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from screens.base_screen import BaseScreen


class Book(Enum):
    Amazing_Words = "Amazing_Words"
    Literature_For_Reading = "Literature_For_Reading"
    TEXT_AND_MORE = "Text_and_More"
    Characters_Words_and_Paragraphs = "Characters_Words_and_Paragraphs"
    A_Book_I_Think = "A_Book_I_Think"


class BooksScreen(BaseScreen):
    screen_id = "SCREEN_BOOKS"

    def open_book(self, book):
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"BOOK_{book}").click()
        except NoSuchElementException:
            max_scrolls = 5
            for _ in range(max_scrolls):
                self.scroll_down()
                try:
                    self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"BOOK_{book}").click()
                    return
                except NoSuchElementException:
                    continue
            print(f"No book with title {book.value}")

    def is_on_book(self, book) -> bool:
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"BOOK_DETAILS_{book.value}")
            return True
        except:
            print(f"{book.value} failed to open")
            return False

    def add_book_as_favourite(self):
        try:
            if self.is_book_favourite() is True:
                print("book already in favourites")
            else:
                self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="BUTTON_SET_BOOK_FAVOURITE").click()
        except:
            print("failed to set title as favourite")

    def remove_books_from_favourites(self):
        try:
            if self.is_book_favourite() is True:
                self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="BUTTON_REMOVE_BOOK_FAVOURITE").click()
            else:
                print("book is not a favourite")
        except NoSuchElementException:
            print("failed to remove book from favourites")

    def is_book_favourite(self) -> bool:
        try:
            if self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="BUTTON_REMOVE_BOOK_FAVOURITE"):
                return True
            else:
                return False
        except NoSuchElementException:
            print("unable to determine favourite status")
            return False
