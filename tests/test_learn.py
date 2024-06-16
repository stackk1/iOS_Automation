from screens.learn_screen import LearnScreen
from screens.launch_screen import LaunchScreen, App


class TestLearn:

    def test_open_learning(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.LEARNING)
        learn_screen = LearnScreen()
        assert learn_screen.is_here()
