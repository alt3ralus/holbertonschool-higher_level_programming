#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        var = a / b
    except ZeroDivisionError:
        return None
    finally:
        if b == 0:
            var = None
        else:
            var = a / b

        print("Inside result: {}".format(var))
        return var
