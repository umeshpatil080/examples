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

# import <module> statement executes the module being imported
from module2 import main # this won't replace 'main()' defined in current module

def main():
    print("In module1 '{}'".format(__name__))

if __name__ == '__main__':
    # Each module will have symbol table with entries for definitions defined in it. It acts as global symbol table for current module.
    # If imported module has same definition defined in it then, definition of construct defined in current modules wiil not get replaced
    main()

    # In conflicting cases, explicit invoke will help you to use definition from imported module
    import module2
    module2.main()
