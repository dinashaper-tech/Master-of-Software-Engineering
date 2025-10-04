"""
Module: analyzer
This module provides classes to analyze strings and lists for length and uppercase count.
"""

from abc import ABC, abstractmethod


class BaseAnalyzer(ABC):
    """Abstract base class for analyzers."""

    def __init__(self, data):
        """
        Initialize with data.
        Args:
            data (str | list): The input data to analyze.
        """
        self.data = data

    @abstractmethod
    def total_length(self):
        """Return the total length of the data."""
        pass

    @abstractmethod
    def uppercase_count(self):
        """Return the number of uppercase characters in the data."""
        pass


class StringAnalyzer(BaseAnalyzer):
    """Analyzer for string inputs."""

    def total_length(self):
        """Return the total length of the string."""
        return len(self.data)

    def uppercase_count(self):
        """Return the count of uppercase characters in the string."""
        return sum(1 for char in self.data if char.isupper())


class ListAnalyzer(BaseAnalyzer):
    """Analyzer for list inputs."""

    def total_length(self):
        """Return the total length of the list."""
        return len(self.data)

    def uppercase_count(self):
        """
        Return the count of uppercase string elements in the list.
        Only considers string elements.
        """
        return sum(
            1 for item in self.data if isinstance(item, str) and item.isupper()
        )


class AnalyzerFactory:
    """Factory to create the correct analyzer based on input type."""

    @staticmethod
    def get_analyzer(data):
        """
        Return the appropriate analyzer for the given data.
        Args:
            data (str | list): The data to analyze.
        Returns:
            BaseAnalyzer: An instance of a suitable analyzer.
        Raises:
            TypeError: If data type is not supported.
        """
        if isinstance(data, str):
            return StringAnalyzer(data)
        if isinstance(data, list):
            return ListAnalyzer(data)
        raise TypeError("Unsupported data type. Must be str or list.")


def main():
    """Main execution function for testing analyzers."""
    # Example string
    string_data = "Hello World"
    string_analyzer = AnalyzerFactory.get_analyzer(string_data)
    print("String Analysis:")
    print("Total Length:", string_analyzer.total_length())
    print("Uppercase Count:", string_analyzer.uppercase_count())

    # Example list
    list_data = ["HELLO", "world", "AI", "Python", 123]
    list_analyzer = AnalyzerFactory.get_analyzer(list_data)
    print("\nList Analysis:")
    print("Total Length:", list_analyzer.total_length())
    print("Uppercase Count:", list_analyzer.uppercase_count())


if __name__ == "__main__":
    main()
