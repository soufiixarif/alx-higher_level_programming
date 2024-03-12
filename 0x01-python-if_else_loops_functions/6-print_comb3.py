#!/usr/bin/python3
for nb in range(0, 10):
    for number in range(1, 10):
        if nb >= number:
            continue
        elif nb == 8 and number == 9:
            print("{}{}".format(nb, number))
        else:
            print("{}{}, ".format(nb, number), end="")
