#!/bin/python3


class FooError(ValueError):
    pass



def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value: %s" % s)
    return 10 / n

try:
    foo('0')
except FooError as f:
    print(f)