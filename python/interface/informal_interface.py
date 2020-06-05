class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass


class PdfParser(InformalParserInterface):
    """Extract text from PDF"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalInterface.extract_text()"""
        pass


class EmlParser(InformalParserInterface):
    """Extract text from an email"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> str:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass


if __name__ == "__main__":
    print("PdfParser is subclass:", issubclass(PdfParser, InformalParserInterface))
    print("EmlParser is subclass:", issubclass(EmlParser, InformalParserInterface))

    print("PdfParser mro:", PdfParser.__mro__)
    print("EmlParser mro:", EmlParser.__mro__)
