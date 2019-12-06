#!/user/bin/python3
def write_file(filename="", text=""):
    """
    open and write a file
    """
    with open(filename, "w", encoding="utf-8") as archive:
        data = archive.write(text)
        archive.close()
    return (data)
