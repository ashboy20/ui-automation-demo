from helpers.driver import Driver
from pages.home import Home


class Pages:
    def __init__(self, driver: Driver):
        self.home = Home(driver)
