#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    i = 1
    if len == 1:
        print("{} argument.".format(len - 1))
    elif len > 1:
        print("{} argument:".format(len - 1))
        while i < len:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
