#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    var = 0
    for count in range(x):
        try:
            print("{:d}".format(my_list[count]), end="")
            var = var + 1
        except TypeError:
            continue
        except ValueError:
            continue
    print()
    return var
