"""Clean Code in Python - Chapter 6: Descriptors

> Types of Descriptors:

    1. Non-Data Descriptors (non-overrindg)
    2. Data Descriptors (overring)

Code examples to illustrate [2].
"""
from log import logger


class DataDescriptor:
    """A descriptor that implements __get__ & __set__."""

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return 42

    def __set__(self, instance, value):
        logger.debug("setting %s. descriptor to %s", instance, value)
        instance.__dict__["descriptor"] = value


class ClientClass:
    descriptor = DataDescriptor()
