from helpers.driver import Driver


class Base:
    def __init__(self, driver: Driver):
        self.driver = driver
