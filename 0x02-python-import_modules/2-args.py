#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    len = len(argv)
    i = 1
    if len == 0:
        print("{} arguments.".format(len))
    elif len == 1:
        print("{} arguments:".format(len))
        print("{}: {}".format(i, sys.argv[1]))
    else:
        print("{} arguments:".format(len))
        while i <= len:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
