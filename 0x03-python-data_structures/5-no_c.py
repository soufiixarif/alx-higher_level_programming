#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for index in my_string:
        if index != 'c' and index != 'C':
            new += index
    return (new)