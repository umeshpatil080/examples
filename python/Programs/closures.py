#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     01/10/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import logging
logging.basicConfig(filename = 'C:\DATA_\Reading Material\Python\Programs\clousure.log', level = logging.INFO)

"""

A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

OR

A closure is the combination of a function and the lexical environment within which that function was declared.

Example:

def init():
    name = 'Mozilla'    # name is a local variable created by init
    def displayName():  # displayName() is the inner function, a closure
        print(name);    # use variable declared in the parent function

    return displayName

"""


def outer_func(msg):
    def inner_func():
        print(msg + " from inner_func")
    return inner_func


def logger(func):
    def log_func(*argv):
        logging.info("Running {} operation with arguments {}".format(func.__name__, *argv))
        result = func(*argv)
        print("Result:{} for operation {}({}, {})".format(result, func.__name__, *argv))
    return log_func

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def main(example = 1):
    if(example == 1):
        hi_clousure = outer_func("Hi")
        hello_clousure = outer_func("Hello")

        hi_clousure()
        hello_clousure()
    elif(example == 2):
        add_clousure = logger(add)
        sub_clousure = logger(sub)

        add_clousure(2, 3)
        sub_clousure(3,1)


if __name__ == '__main__':
    print("Clousure exampl 1")
    main(1)

    print("\nClousure exampl 2")
    main(2)
