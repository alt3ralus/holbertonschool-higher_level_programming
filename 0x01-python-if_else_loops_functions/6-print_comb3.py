#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if y > x:
            print("{}{}".format(x, y), end="")
            if (x < 8 or y < 9):
                print(",", end=" ")
print()
