import abc
from abc_base import PluginBase


@PluginBase.register
class IncompleteImplementation(PluginBase):
    def save(self, output, data):
        return output.write(data)


if __name__ == "__main__":
    print("Subclass:", issubclass(IncompleteImplementation, PluginBase))
    print("Instance:", isinstance(IncompleteImplementation(), PluginBase))
