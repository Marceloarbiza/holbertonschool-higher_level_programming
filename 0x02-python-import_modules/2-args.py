#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    len = len(argv)
    i = 1
    if len is 0:
        print("{} argument.".format(len))
    elif len is 1:
        print("{} argument:".format(len))
        print("{}: {}".format(i, sys.argv[1]))
    else:
        print("{} argument:".format(len))
        while i <= len:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
