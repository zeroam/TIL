import abc
import io


class ABCWithConcreteImplementation(abc.ABC):
    @abc.abstractmethod
    def retrieve_values(self, input):
        print("Base class reading data")
        return input.read()


class ConcreteOverride(ABCWithConcreteImplementation):
    def retrieve_values(self, input):
        base_data = super(ConcreteOverride, self).retrieve_values(input)
        print("subclass sorting data")
        response = sorted(base_data.splitlines())
        return response


input = io.StringIO(
    """line one
line two
line three
"""
)

reader = ConcreteOverride()
print(reader.retrieve_values(input))
print()
