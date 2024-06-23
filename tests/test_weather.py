#Tests for Weather App - Andrew Stack 2024
from screens.weather_screen import WeatherScreen
from screens.launch_screen import LaunchScreen, App


class TestWeather:

    def test_open_weather(self):
        launch_screen = LaunchScreen()
        launch_screen.launch_app(App.WEATHER)
        weather_screen = WeatherScreen()
        assert weather_screen.is_here()
