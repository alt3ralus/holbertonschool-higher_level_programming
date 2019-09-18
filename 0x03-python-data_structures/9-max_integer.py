#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    if my_list is not None:
        my_list.sort()
        my_list.sort(reverse=True)
        return my_list[0]
