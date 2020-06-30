import pytest
import requests


@pytest.fixture(autouse=True)
def disable_network_call(monkeypatch):
    def stuned_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stuned_get())


@pytest.fixture
def input_value():
    return 39
