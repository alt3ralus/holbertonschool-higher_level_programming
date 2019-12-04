#!/usr/bin/python3


class Rectangle:
    """Construct method"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width > 0 and self.__height > 0:
            return (self.__width + self.__height) * 2
        else:
            return 0

    def __str__(self):
        cadena = []
        if self.__width == 0 or self.__height == 0:
            return ('')

        for i in range(self.__height):
            for j in range(self.__width):
                cadena.append(self.print_symbol)
            if i is not self.__height - 1:
                cadena.append('\n')
        return "".join(cadena)

    def __repr__(self):

        cdn = "Rectangle({:d}, {:d})".format(eval(str(self.__width)),
                                             eval(str(self.__height)))
        return(cdn)

    def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
