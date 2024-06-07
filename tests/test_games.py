from screens.games_screen import GamesScreen, Game
from screens.launch_screen import LaunchScreen, App
import pytest

class TestGames:

    def test_open_games(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        assert games_screen.is_here()

    def test_open_slots(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        games_screen.go_to_game(Game.SLOTS)
        assert games_screen.is_on_game(Game.SLOTS)

    @pytest.mark.parametrize(
        "game",
        [game for game in Game]
    )
    def test_open_game(self, game: Game):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        games_screen.go_to_game(game)
        assert games_screen.is_on_game(game)
