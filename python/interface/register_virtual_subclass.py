import abc


class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number"""

    pass


@Double.register
class Double64:
    """A 64-bit double-precision floating-point number"""

    pass


Double.register(float)


if __name__ == "__main__":
    print("float is subclass of Double:", issubclass(float, Double))
    print("1.2345 is instance of Double:", isinstance(1.2345, Double))
    print("Double64 is subclass of Double:", issubclass(Double64, Double))
