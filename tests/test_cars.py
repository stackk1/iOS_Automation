from screens.cars_screen import CarsScreen
from screens.launch_screen import LaunchScreen, App


class TestCars:

    def test_open_cars(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.CARS)
        cars_screen = CarsScreen()
        assert cars_screen.is_here()

    def test_go_to_car(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.CARS)
        cars_screen = CarsScreen()
        cars_screen.go_to_car("BAJA","2003")
        assert cars_screen.get_car_detail("MODEL") == "Baja"
        assert cars_screen.get_car_detail("YEAR") == "2003"
