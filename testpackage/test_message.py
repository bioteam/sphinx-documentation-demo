from __future__ import annotations

class TestMessage(object):
    """This is the docstring for the TestMessage class.

    Args:
        message_string (string): String to be printed later
    """
    def __init__(self, message_string: str):
        self.message_string = message_string

    @staticmethod
    def from_number(number: int) -> TestMessage:
        """Creates a TestMessage from the provided number.

        Args:
            number: the number to convert into a string
        """

        return TestMessage(message_string=str(number))

