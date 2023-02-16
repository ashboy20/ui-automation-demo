from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from pages.base import Base


class Home(Base):
    @property
    def btn_login(self) -> WebElement:
        return self.driver.find_element(AppiumBy.ID, "xxxx")

    @property
    def input_username(self) -> WebElement:
        return self.driver.find_element(AppiumBy.ID, "xxxx")

    def here(self) -> bool:
        return self.btn_login.is_displayed()

    def login(self, username: str):
        self.input_username.send_keys(username)
        self.btn_login.click()
