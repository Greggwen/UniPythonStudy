#!/bin/python3

import logging

logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)

    # 断言
    assert n != 0, 'n is zero'

    # logging
    logging.info('n = %d' % n)
    return 10 / n

def main ():
    foo('0')

main()