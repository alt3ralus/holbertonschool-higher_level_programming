#!/usr/bin/python3
class BaseGeometry():
    """
    Base Class
    """
    def area(self):
        """
        method returns an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that validates the parameters
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
