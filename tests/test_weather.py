#Tests for Weather App - Andrew Stack 2024
from screens.weather_screen import WeatherScreen
from screens.launch_screen import LaunchScreen


class TestWeather:

    def test_open_weather(self):
        launch_screen = LaunchScreen()
        launch_screen.go_to_weather_screen()
        weather_screen = WeatherScreen()
        assert weather_screen.is_here()
