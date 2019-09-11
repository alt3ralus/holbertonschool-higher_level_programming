#!/usr/bin/python3
def uppercase(str):
    for count in str:
        if(ord(count) >= 97 and ord(count) <= 122):
            count = chr(ord(count) - 32)
        print("{:s}".format(count), end="")
    print("")
