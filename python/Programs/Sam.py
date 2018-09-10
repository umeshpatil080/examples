#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     05/08/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pprint
import sys

def test(**kwargs):
    for key, val in kwargs.items():
        print ("Key:%s\tValue:%s" % (str(key), str(val)))

def main():
    #test(a = 1, b= 2)
    sys.stdout.write("line1")
    sys.stdout.write("line2")


if __name__ == '__main__':
    main()
