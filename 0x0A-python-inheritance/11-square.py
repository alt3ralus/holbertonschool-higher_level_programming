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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    creating a subclass from BaseGeometry class
    """
    def __init__(self, width, height):
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """
        method to obtain the rectangle area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        metadata of the rectangle
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
    creating a subclass Square from class parent Rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return("[Square] {}/{}".format(self.__size, self.__size))
