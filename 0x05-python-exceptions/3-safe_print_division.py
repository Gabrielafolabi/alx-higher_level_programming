#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division = a / b
    except (ZeroDivisionError, TypeError):
        division = none
    finally:
        print("Inside Result: {}" .format(division))
    return(division)


