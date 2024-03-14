#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    name = sys.argv
    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("{} argument:".format(ac))
    else:
        print("{} arguments :".format(ac))
    if ac >= 1:
        ac = 0
        for arg in sys.argv:
            if ac != 0:
                print("{}: {}".format(ac, arg))
            ac += 1
