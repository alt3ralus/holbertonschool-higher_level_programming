#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv) - 1

    if args == 1:
        print("{:d} argument:".format(args))
        print("1: {}".format(argv[1]))
    elif args == 0:
        print("{:d} arguments.".format(args))
    else:
        print("{:d} arguments:".format(args))
        for count in range(1, args + 1):
            print("{:d}: {}".format(count, argv[count]))
