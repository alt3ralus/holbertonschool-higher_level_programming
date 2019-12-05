#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    if use isinstance the result will be True for int and float,
    but with the type is:  the result is the expected
    """
    if type(obj) is a_class:
        return True
    return False
