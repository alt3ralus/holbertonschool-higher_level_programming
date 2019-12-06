#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    program to open an count every inside line
    """
    with open(filename, mode="r", encoding="utf-8") as archive:

        count = 0
        while True:
            data = archive.readline()
            if not data:
                break
            count += 1
        return count
