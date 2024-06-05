from screens.cars_screen import CarsScreen
from screens.launch_screen import LaunchScreen


class TestCars:

    def test_open_cars(self):
        launch_screen = LaunchScreen()
        launch_screen.go_to_cars_screen()
        cars_screen = CarsScreen()
        assert cars_screen.is_here()
