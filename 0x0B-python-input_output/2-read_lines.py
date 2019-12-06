#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    function that prints n line of the text.
    """
    count = 0

    with open(filename, "r", encoding="utf-8") as archive:

        with open(filename, "r") as f:
            for line in f:

                count += 1

                if nb_lines <= 0 or (count <= nb_lines and nb_lines > 0):
                    print(line, end="")
                else:
                    break
