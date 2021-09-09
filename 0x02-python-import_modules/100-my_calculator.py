#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    operators = ['+', '-', '*', '/']
    argv = sys.argv[1:]
    leni = len(argv)

    if leni != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        for i in operators:
            if sys.argv[2] == i:
                a = int(sys.argv[1])
                b = int(sys.argv[3])

                if sys.argv[2] == '+':
                    print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
                elif sys.argv[2] == '-':
                    print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
                elif sys.argv[2] == '*':
                    print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
                elif sys.argv[2] == '/':
                    print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
