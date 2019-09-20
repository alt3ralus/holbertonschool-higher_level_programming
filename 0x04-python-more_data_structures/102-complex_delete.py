#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = a_dictionary.copy()
    for key in new_dic:
        if a_dictionary[key] == value:
            a_dictionary.pop(key)
    return a_dictionary
