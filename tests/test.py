from helpers.driver import Driver
from pages import Pages
from steps.steps import LoginSteps


def test_first(steps: LoginSteps):
    steps.user_is_on_login_page()
    steps.login()


def run():
    driver = Driver()
    pages = Pages(driver)
    steps = LoginSteps(pages)
    test_first(steps)


if __name__ == '__main__':
    run()
