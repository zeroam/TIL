"""Clean Code in Python - Chapter 6: Descriptors

> Using descriptors instead of class decorators

"""
from datetime import datetime
from functools import partial
from typing import Any, Callable


class BaseFieldTransformation:
    """Base class to define descriptors that convert values."""

    def __init__(self, transformation: Callable[[Any, str], str]) -> None:
        self._name = None
        self.transformation = transformation

    def __get__(self, instance, owner):
        if instance is None:
            return self
        raw_value = instance.__dict__[self._name]
        return self.transformation(raw_value)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value


showOriginal = partial(BaseFieldTransformation, transformation=lambda x: x)
HideField = partial(
    BaseFieldTransformation, transformation=lambda x: "**redacted**"
)
FormatTime = partial(
    BaseFieldTransformation,
    transformation=lambda ft: ft.strftime("%Y-%m-%d %H:%M"),
)


class LoginEvent:
    """
    >>> le = LoginEvent(
    ... "usr", "secret password", "127.0.0.1", datetime(2016, 7, 20, 15, 45)
    ... )
    >>> vars(le)
    {'username': 'usr', 'password': 'secret password', 'ip': '127.0.0.1', 'timestamp': datetime.datetime(2016, 7, 20, 15, 45)}

    >>> le.serialize()
    {'username': 'usr', 'password': '**redacted**', 'ip': '127.0.0.1', 'timestamp': '2016-07-20 15:45'}

    >>> le.password
    '**redacted**'

    """

    username = showOriginal()
    password = HideField()
    ip = showOriginal()
    timestamp = FormatTime()

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self):
        return {
            "username": self.username,
            "password": self.password,
            "ip": self.ip,
            "timestamp": self.timestamp,
        }
