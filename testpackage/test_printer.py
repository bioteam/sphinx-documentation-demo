from __future__ import annotations
from testpackage.test_message import TestMessage

class TestPrinter(object):
    """This is the docstring for TestPrinter
    Stuff
    
    Args:
        msg: Message to be stored for later printing
    """

    def __init__(self, msg: TestMessage):
        self.msg = msg


    def print(self) -> None:
        """This function is used to print the stored message.
        """
        print(self.msg.message_string)


def function_within_package() -> None:
    """This is just an example of a function within a package 
    that is not also contained within a class.
    """
    print("This is a test function")

