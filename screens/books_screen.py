from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from screens.base_screen import BaseScreen
from tests.fixtures.value_checker import ValueChecker


class Book(Enum):
    Amazing_Words = "Amazing_Words"
    Literature_For_Reading = "Literature_For_Reading"
    TEXT_AND_MORE = "Text_and_More"
    Characters_Words_and_Paragraphs = "Characters_Words_and_Paragraphs"
    A_Book_I_Think = "A_Book_I_Think"


class BooksScreen(BaseScreen):
    screen_id = "SCREEN_BOOKS"

    def open_book_details(self, book):
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"BOOK_{book}").click()
        except NoSuchElementException:
            print(f"Unable to find {book.value} in list")

    def is_on_book_details(self, book) -> bool:
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"BOOK_DETAILS_{book.value}")
            return True
        except NoSuchElementException:
            print(f"{book.value}details page failed to open")
            return False

    def add_book_as_favourite(self):
        try:
            if self.is_book_favourite() is True:
                print("book already in favourites")
            else:
                self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="BUTTON_SET_BOOK_FAVOURITE").click()
        except NoSuchElementException:
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

    def open_book(self):
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="BUTTON_READ_BOOK").click()
        except NoSuchElementException:
            print("failed to launch book reader")

    def is_on_book(self, book) -> bool:
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SCREEN_BOOK_READER")
            return True
        except NoSuchElementException:
            print(f"{book} failed to open")
            return False

    def get_page_number(self):
        current_page = ValueChecker.get_value(self, "BOOK_PAGE_NUMBER")
        print(current_page)
        return current_page