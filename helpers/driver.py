from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Driver:
    def __init__(self):
        caps = {
            "appium:automationName": "UiAutomator2",
            "platformName": "Android",
            "appium:deviceName": "R5CR92L36NE",
            "appium:bundleId": "co.mona.android.staging.dex.auto.test",
            "appium:fullReset": False,
            "appium:noSign": True
        }

        # appium 2.0 does not need `wd/hub` in the host
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self._default_wait = WebDriverWait(self._driver, 3)

    def teardown(self):
        if self._driver:
            self._driver.quit()

    def find_element(self, by: str, value: str) -> WebElement:
        # you can make customization for your project
        # TODO: apply custom webdriver wait
        return self._default_wait.until(EC.visibility_of_element_located((by, value)))
