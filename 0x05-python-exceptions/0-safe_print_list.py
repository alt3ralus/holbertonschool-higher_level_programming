#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for count in range(x):
                print('{}'.format(my_list[count]), end="")
        print()

        return x

    except IndexError:
        print()
        return count
