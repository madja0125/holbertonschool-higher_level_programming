#!/bin/usr/python3

def print_sorted_dictionary(a_dictionary):

    ordered = sorted(a_dictionary.keys())

    for key in ordered:
        print(f"{key}: {a_dictionary[key]}")
