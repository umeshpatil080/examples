#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     15/10/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
    finally block always executes ireespective of error is encountered or caught using except or even if no matching except is present.
"""
def sam(a, b):
    try:
        print("Inputs a={} b={}".format(a, b))
        c = a / b
    except ZeroDivisionError as ex:
        print("Encountered divide by zero error")
    else:
        print("No error is hit")
    finally:
        print("Cleaning up in finally\n\n")


def main():
    sam(1,2)
    sam(1,0)
    sam('1', 2)

if __name__ == '__main__':
    main()
