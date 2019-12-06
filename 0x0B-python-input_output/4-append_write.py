#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    open and append some text to a existing file
    """

    with open(filename, "a",  encoding="utf-8") as archive:
        data = archive.write(text)
        archive.close()
        return data
