#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cadena = []
    for count in my_list:
        if count % 2 == 0:
            cadena.append(True)
        else:
            cadena.append(False)
    return cadena
