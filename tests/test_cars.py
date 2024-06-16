from screens.cars_screen import CarsScreen
from screens.launch_screen import LaunchScreen, App


class TestCars:

    def test_open_cars(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.CARS)
        cars_screen = CarsScreen()
        assert cars_screen.is_here()
