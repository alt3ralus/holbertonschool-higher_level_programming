#!/usr/bin/python3
def lookup(obj):
    """creates a list with all object's attributes and methods """
    lista = list(dir(obj))
    return lista
