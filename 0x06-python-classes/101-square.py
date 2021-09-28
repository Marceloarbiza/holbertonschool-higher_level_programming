#!/usr/bin/python3
"""Doc"""


class Square:
    """Define new atribute Position"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        if isinstance(self.__size, int) is False:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

        if type(self.__position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(isinstance(i, int) is False for i in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(i < 0 for i in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for h in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end="")
                for j in range(self.__size):
                    print('#', end="")
                print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(isinstance(i, int) is False for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
