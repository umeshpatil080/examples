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

class CustomError(Exception):
    """
        User defined exception class should inherit from 'Exception' class either directly or indirectly.
    """

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

def main():
    try:
        raise CustomError("field1 value", "field2 value")
    except CustomError as ex:
        print("__class__:{}".format(ex.__class__))
        print("type:{}".format(type(ex)))
        print("CustomError occured\nfield1:{}\nfield2:{}\n".format(ex.field1, ex.field2))

if __name__ == '__main__':
    main()
