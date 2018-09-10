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


import sys

def main():
    try:
        #a = 1/0
        b = int('21a')

    except (ZeroDivisionError, ValueError) as ex:
        print("Encountered error:{}".format(ex))
    except:
        """
        Generic exception handler.
        Gets executed if there is no matching exception handler is in place.
        """
        print("Unexpected error: {}".format(sys.exc_info()[0]))
    else:
        """
        Must be after all 'except' block(s).
        Will execute if there is no exception.
        """
        print("In else part")

if __name__ == '__main__':
    main()
