#!/usr/bin/python3
for nb in range(0, 100):
    print(str(nb).zfill(2), end="")
    if nb != 99:
        print(", ", end="")
