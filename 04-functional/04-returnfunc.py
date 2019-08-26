#!/bin/python3


def lazy_sum(*args):
    def sum ():
        ax = 0
        for i in args:
            ax = ax + i
        return ax 
    return sum


fsum = lazy_sum(1, 2, 3, 4, 5, 6, 7)

print(fsum)
print(fsum())
