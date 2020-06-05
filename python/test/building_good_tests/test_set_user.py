import pytest


@pytest.fixture
def user():
    return User(name="Chris", hair_color=Color("brown"))


@pytest.fixture(autouse=True)
def set_user(client, user):
    client.set_user(user)


def test_set_user(client, user):
    # client.get_user() returns another User object
    assert client.get_user() == user
