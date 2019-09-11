#!/usr/bin/python3
for count in reversed(range(97, 123)):
    cadena = chr(count)
    if count % 2 != 0:
        cadena = chr(count - 32)
    print("{}".format(cadena), end="")
