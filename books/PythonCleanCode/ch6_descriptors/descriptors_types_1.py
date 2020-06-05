"""Clean Code in Python - Chapter 6: Descriptors

> Types of Descriptors:

    1. Non-Data Descriptors (non-overriding)
    2. Data Descriptors (overriding)

Code examples to illustrate [1].
"""


class NonDataDescriptor:
    """A descriptor that doesn't implement __set__."""
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return 42


class ClientClass:
    descriptor = NonDataDescriptor()
