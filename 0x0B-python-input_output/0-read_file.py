#!/usr/bin/python3
def read_file(filename=""):
    """
    program to open an print a file.
    """
    with open(filename, mode="r", encoding="utf-8") as data:
        archive = data.read()
    print(archive)
