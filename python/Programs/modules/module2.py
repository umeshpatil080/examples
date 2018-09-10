#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     14/10/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("In module2 '{}'".format(__name__))

if __name__ == '__main__':
    main()

print("In module2 non __name__ check")
