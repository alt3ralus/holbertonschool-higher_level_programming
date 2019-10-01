#!/usr/bin/python3
class Square():
    """Defining an private instance attribute"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__value = value

    def area(self):
        """
        definig area
        """
        return self.__size**2
