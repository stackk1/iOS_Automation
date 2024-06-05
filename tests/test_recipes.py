from screens.recipes_screen import RecipeScreen
from screens.launch_screen import LaunchScreen


class TestCarList:

    def test_open_recipes(self):
        launch_screen = LaunchScreen()
        launch_screen.go_to_recipes_screen()
        recipe_screen = RecipeScreen()
        assert recipe_screen.is_here()
