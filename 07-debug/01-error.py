#!/bin/python3

try:
    print("try...")
    r = 10 / int('a')
    print("result:", r)
except ZeroDivisionError as e:
    print("except:", e)
except ValueError as v:
    print("except:", v)
finally:
    print("finally")

print("End")