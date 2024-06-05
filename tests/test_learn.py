from screens.learn_screen import LearnScreen
from screens.launch_screen import LaunchScreen


class TestLearn:

    def test_open_learning(self):
        launch_screen = LaunchScreen()
        launch_screen.go_to_learning_screen()
        learn_screen = LearnScreen()
        assert learn_screen.is_here()
