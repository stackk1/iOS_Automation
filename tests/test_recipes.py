from screens.recipes_screen import RecipeScreen
from screens.launch_screen import LaunchScreen, App


class TestCarList:

    def test_open_recipes(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.RECIPES)
        recipe_screen = RecipeScreen()
        assert recipe_screen.is_here()
