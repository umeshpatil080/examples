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

def main():
    try:
        ex = Exception("sam1", "sam2")
        raise ex
    except Exception as ex:
        print(type(ex))     # Exception type
        print(ex.args)      # arguments stored in .args
        print(ex)           # __str__ prints .args. Can be overwritten in  exception subclass

if __name__ == '__main__':
    main()
