#!/bin/usr/python3

def search_replace(my_list, search, replace):

    if my_list is None:
        return

    if len(my_list) == 0:
        return

    new_list = my_list.copy()

    for i in range(len(new_list)):
            if new_list[i] == search:
                new_list[i] = replace

    return new_list
