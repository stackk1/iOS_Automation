from screens.games_screen import GamesScreen, Game
from screens.launch_screen import LaunchScreen, App
import pytest


class TestGames:

    def test_open_games(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        assert games_screen.is_here()

    @pytest.mark.parametrize(
        "game",
        [game for game in Game]
    )
    def test_open_game(self, game: Game):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        games_screen.go_to_game(game.value)
        assert games_screen.is_on_game(game.value)

    def test_open_settings(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        games_screen.go_to_settings()
        assert games_screen.is_on_game_settings()

    def test_slots(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        games_screen.go_to_game("SLOTS")
        games_screen.press_button("SPIN")
        score = games_screen.get_slot_score()
        assert score != 1000

    def test_war(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        games_screen.go_to_game("WAR")
        games_screen.press_button("DEAL")
        cards_left = games_screen.get_war_cards_remaining()
        assert cards_left != 104

    def test_dice_war(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        games_screen.go_to_game("DICE_WAR")
        games_screen.press_button("ROLL")
        dice_score = games_screen.get_dice_war_score()
        assert dice_score != 0

    def test_dice_roller(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        games_screen.go_to_game("DICE_ROLLER")
        games_screen.press_button("ROLL")
        assert games_screen.get_dice_roller_count() != 0

    def test_card_flipper(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.GAMES)
        games_screen = GamesScreen()
        games_screen.go_to_game("CARD_FLIPPER")
        first_card = games_screen.get_card_flipper_value()
        games_screen.swipe(800, 500, 200, 500)
        second_card = games_screen.get_card_flipper_value()
        assert first_card != second_card