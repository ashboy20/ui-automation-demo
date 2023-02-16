from hamcrest import assert_that

from pages import Pages


class LoginSteps:
    def __init__(self, pages: Pages):
        self.pages = pages

    def user_is_on_login_page(self):
        assert_that(self.pages.home.here(), "User is not redirected to home page")

    def login(self):
        self.pages.home.login("username")
        # assert_that(pages.next_page.here(), "reason to failure")
