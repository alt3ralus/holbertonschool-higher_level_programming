#!/usr/bin/python3
class Square():
    """Defining an private instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value(type) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(tuple) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0](type) is not int and value[1](type) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        def area
        """
        return self.__size**2

    def my_print(self):
        if self.size == 0 or self.size < 0:
            print()
        else:
            for count in range(self.size):
                print("#" * self.size)
                print(" " * self.__position[0])
