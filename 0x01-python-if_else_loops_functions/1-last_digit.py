#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
cadena1 = "and is less than 6 and not 0"
cadena2 = "and is zero"
cadena3 = "and is greater than 5"
if number < 0:
    var = (-number % 10) * -1
elif number > 0:
    var = number % 10
if var < 6:
    print("Last digit of {:d} is {:d} {}".format(number, var, cadena1))
elif var == 0:
    print("Last digit of {:d} is {:d} {}".format(number, var, cadena2))
elif var > 5:
    print("Last digit of {:d} is {:d} {}".format(number, var, cadena3))
