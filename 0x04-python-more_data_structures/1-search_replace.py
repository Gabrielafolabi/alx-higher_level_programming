#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if my_list:
        new_list = list(map(lambda a: a if a != search else replace, my_list))
    return new_list
