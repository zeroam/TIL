import pytest


def is_palinedrome(word: str):
    word = word.replace(" ", "")
    return word.lower() == word[::-1].lower()


@pytest.mark.parametrize("palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(palindrome, expected_result):
    assert is_palinedrome(palindrome) == expected_result
