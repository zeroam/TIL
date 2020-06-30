import pytest
import requests


def test_requests():
    with pytest.raises(RuntimeError):
        resp = requests.get("https://google.com")
