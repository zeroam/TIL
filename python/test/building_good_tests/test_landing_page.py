import pytest


class LoginPage:
    def __init__(self, driver):
        self.driver = driver


class LandingPage:
    def __init__(self, driver):
        self.driver = driver


class TestAfterLogin:
    @pytest.fixture(scope="class", autouse=True)
    def login_page(self, driver):
        driver.get("https://www.mysite.com/login")
        page = LoginPage(driver)
        return page

    @pytest.fixture(scope="class", autouse=True)
    def login(self, login_page):
        login_page.login(username="username", password="password")

    @pytest.fixture(scope="class", autouse=True)
    def page(self, driver):
        return LandingPage(driver)

    def test_title(self, page):
        assert page.title == "Welcome"
