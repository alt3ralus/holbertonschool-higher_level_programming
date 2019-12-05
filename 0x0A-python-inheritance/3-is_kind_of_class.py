#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Asking if an instance is an object from the class
    """
    if isinstance(obj, a_class):
        return True
    return False
