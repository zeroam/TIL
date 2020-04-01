"""Clean Code in Python - Chater 4, The SOLID Principles

> Liskov's Substitution Principle (LSP)

Detecting violatinos os LSP through tools (mypy, pylint, etc.)
"""


class Event:
    ...

    def meets_condition(self, event_data: dict) -> bool:
        return False


class LoginEvent(Event):
    def meets_condition(self, event_data: list) -> bool:  # type: ignore
        return bool(event_data)


class LogoutEvent(Event):
    def meets_condition(self, event_data: dict, override: bool) -> bool:  # type: ignore
        if override:
            return True
        ...
