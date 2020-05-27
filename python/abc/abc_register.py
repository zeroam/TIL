import abc
from abc_base import PluginBase


class LocalBaseClass:
    pass


@PluginBase.register
class RegisterImplementation(LocalBaseClass):
    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == "__main__":
    print("Subclass:", issubclass(RegisterImplementation, PluginBase))
    print("Instance:", isinstance(RegisterImplementation(), PluginBase))
