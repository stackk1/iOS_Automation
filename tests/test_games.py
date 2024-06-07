from screens.games_screen import GamesScreen
from screens.launch_screen import LaunchScreen

class TestGames:

    def test_open_games(self):
        launch_screen = LaunchScreen()
        launch_screen.go_to_games_screen()
        games_screen = GamesScreen()
        assert games_screen.is_here()

    def test_open_slots(self):
        launch_screen = LaunchScreen()
        launch_screen.go_to_games_screen()
        games_screen = GamesScreen()
        games_screen.go_to_slots()
        assert games_screen.is_on_slots_screen()