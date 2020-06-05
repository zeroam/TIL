import abc


class PluginBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source
        and return an object"""

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output"""
