#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        x = number % 10
        print('{:d}'.format(x), end='')
    elif number < 0:
        num = number * -1
        x = num % 10
        print('{:d}'.format(x), end='')
    return x
