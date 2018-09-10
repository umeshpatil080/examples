#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     17/09/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def is_palindrome(**kwargs):
    str = kwargs['data']
    i = 0
    j = len(str) - 1
    while(i < j and str[i] == str[j]):
        i = i+ 1
        j = j - 1
    if(j <= i):
        print("%s is plaindrome" % str)
    else:
        print("%s is not plaindrome" % str)

def main():
    is_palindrome( data = "saabaas")

if __name__ == '__main__':
    main()
