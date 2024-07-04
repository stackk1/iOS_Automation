import pytest
from screens.books_screen import BooksScreen, Book
from screens.launch_screen import LaunchScreen, App


class TestBooks:

    def test_open_books(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.BOOKS)
        books_screen = BooksScreen()
        assert books_screen.is_here()

    @pytest.mark.parametrize(
        "book",
        [book for book in Book]
    )
    def test_open_book(self, book: Book):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.BOOKS)
        books_screen = BooksScreen()
        books_screen.open_book(book.value)

        assert books_screen.is_on_book(book.value)