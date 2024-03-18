#!/usr/bin/python3
def no_c(my_string):
    charlist = list(my_string)
    for chr in charlist:
        if chr == 'c' or chr == 'C':
            charlist.remove(chr)
    return("".join(charlist))
