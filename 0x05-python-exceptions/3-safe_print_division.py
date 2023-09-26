#!/usr/bin/python3
def safe_print_division(a, b):
    '''divides two numbers and raises exceptions'''
    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("{}".format(res))
