from screens.books_screen import BooksScreen
from screens.launch_screen import LaunchScreen


class TestBooks:

    def test_open_books(self):
        launch_screen = LaunchScreen()
        launch_screen.go_to_books_screen()
        books_screen = BooksScreen()
        assert books_screen.is_here()