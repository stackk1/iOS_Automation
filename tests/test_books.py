from screens.books_screen import BooksScreen
from screens.launch_screen import LaunchScreen, App


class TestBooks:

    def test_open_books(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.BOOKS)
        books_screen = BooksScreen()
        assert books_screen.is_here()