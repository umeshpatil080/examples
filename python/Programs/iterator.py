#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     24/09/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def for_loop_iteration():
    list_items = [1, 2, 3, 4, 5]
    sys.stdout.write("List items:")
    for item in list_items:
        sys.stdout.write("{0}\t".format(item))

    # for loop is implemented as infinite while loop

    iterator = iter(list_items)
    sys.stdout.write("\nList items:")
    while True:
        try:
            element = next(iterator)
            sys.stdout.write("{0}\t".format(element))
        except StopIteration:
            break

class PoweTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    # Method name should be '__next__' but it is expecting method name to be 'next'.
    # It could be issue with python version being used to run this code.
    def next(self):
        self.n = self.n + 1
        if(self.n > self.max):
            raise StopIteration

        sqr_val = self.n ** 2
        return sqr_val


def main():
    for_loop_iteration()

    print("Custom iterator\n")
    for i in PoweTwo(5):
        print(i)

    print("Explicit custom iterator usage")
    pwr = PoweTwo(2)
    iterator = iter(pwr)
    try :
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
    except StopIteration:
        print("End of iteration hit")


if __name__ == '__main__':
    main()
