#!/usr/bin/python3
def remove_char_at(str, n):
    ptr = ""
    for i in range(len(str)):
        if i != n:
            ptr += str[i]
    return ptr
