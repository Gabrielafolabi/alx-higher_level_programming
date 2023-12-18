#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division = a / b
    except TypeError:
        division = none
    except ZeroDivisionError:
        division = none
    finally:
        print("Inside result: {}".format(division))
    return(division)
