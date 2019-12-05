#!/usr/bin/python3
class MyList(list):
    """ creating parent class"""
    def print_sorted(self):
        """ printing the sorted list"""
        self = list(sorted(self))
        print(self)
