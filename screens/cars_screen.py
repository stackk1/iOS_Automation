from appium.webdriver.common.appiumby import AppiumBy

from screens.base_screen import BaseScreen


class CarsScreen(BaseScreen):
    screen_id = "SCREEN_CARS"

    def go_to_car(self, model, year):
        try:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"CARCARD_{model}_{year}").click()
        except:
            print(f"Failed to click CARCARD")

    def get_car_detail(self, spec):
        detail_value = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"CAR_CURRENT_{spec}_VALUE").text
        return detail_value