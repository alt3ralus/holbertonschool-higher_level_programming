#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    var = 0
    new_list = []

    if idx < 0 or idx >= len(my_list) or len(my_list) == 0:
        return my_list
    for count in range(len(my_list)):
        var = my_list[idx]
        my_list.remove(var)

        new_list = my_list.copy()
        return new_list
