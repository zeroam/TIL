"""Avoid multiple asserts"""
import pytest


class Apple:
    color = "Green"
    worms = ["worm"]

    def is_sweet(self):
        return False


@pytest.fixture(scope="class")
def apple():
    return Apple()


class TestApple:
    def test_is_sweet(self, apple):
        assert apple.is_sweet()

    def test_color_is_red(self, apple):
        assert apple.color == "Red"

    def test_has_no_worms(self, apple):
        assert len(apple.worms) == 0
