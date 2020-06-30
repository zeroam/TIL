import pytest


def is_palinedrome(word: str):
    word = word.replace(" ", "")
    return word.lower() == word[::-1].lower()


@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God",
])
def test_is_palindrome(palindrome):
    assert is_palinedrome(palindrome)


@pytest.mark.parametrize("non_palindrome", [
    "abc",
    "abab",
])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palinedrome(non_palindrome)
