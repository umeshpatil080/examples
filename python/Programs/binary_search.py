#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     16/09/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def binary_search(key, arr):
    if(len(arr) > 0):
        mid = len(arr)/2
        if(arr[mid] == key):
            print ("Key %d found " % (key))
            return True
        elif(key < arr[mid]):
            binary_search(key, arr[0:mid])
        else:
            binary_search( key, arr[mid+1: len(arr)])
    else:
        print ("key %d not found." % (key))
        return False

def main():
   nums = [1, 2, 3, 4, 5, 6, 7, 8]
   key = 8
   binary_search(key, nums)

if __name__ == '__main__':
    main()
