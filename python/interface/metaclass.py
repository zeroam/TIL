class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation"""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, "load_data_source")
            and callable(subclass.load_data_source)
            and hasattr(subclass, "extract_text")
            and callable(subclass.extract_text)
        )


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """

    pass


class PdfParserNew:
    """Extract text from a PDF"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass


class EmlParserNew:
    """Extract text from an email"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser
        Does not override UpdatedInformalParserInterface.extract_text()
        """
        pass


if __name__ == "__main__":
    print(
        "PdfParsreNew is subclass:",
        issubclass(PdfParserNew, UpdatedInformalParserInterface),
    )
    print(
        "EmlParserNew is subclass:",
        issubclass(EmlParserNew, UpdatedInformalParserInterface),
    )

    print("PdfParserNew mro:", PdfParserNew.__mro__)
    print("EmlParserNew mro:", EmlParserNew.__mro__)
