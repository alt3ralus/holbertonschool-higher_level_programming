#!/usr/bin/python3
class MyInt(int):
    """
    creating a class
    """
    def __eq__(self, value):
        """
        change default value
        """
        return False

    def __ne__(self, value):
        """
        change the default value of the method
        """
        return True
