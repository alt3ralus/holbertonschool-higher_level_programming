#!/usr/bin/python3
def uniq_add(my_list=[]):

    new_list = list(set(my_list))
    result = 0

    for count in new_list:
        result += count
    return result
