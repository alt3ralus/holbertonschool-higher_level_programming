#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    object is an instance of a class that inherited from an specific class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
