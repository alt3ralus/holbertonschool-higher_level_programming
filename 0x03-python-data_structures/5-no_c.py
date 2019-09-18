#!/usr/bin/python3
def no_c(my_string):
    cadena = ""
    for x in my_string:
        if x != "c" and x != "C":
            cadena = cadena + x
    return cadena
