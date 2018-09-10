#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     02/10/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""

Decorator is a function which takes another function as an argument and returns a function.

"""

def my_decorator(f):
    def wrapper():
        print("Before calling method '{}()'".format(f.__name__))
        f()
        print("After calling method '{}()'".format(f.__name__))

    return wrapper

#-------- 1 --------
def func():
    print("In function 'func()'")

#-------- 2 --------
@my_decorator
def implicit_decorator():
    print("Inside 'implicit_decorator()'")


def my_decorator_with_args(f):
    def wrapper(*args, **kwargs):
        print("Before calling method '{}()'".format(f.__name__))
        f(*args, **kwargs)
        print("After calling method '{}()'".format(f.__name__))

    return wrapper

#------- 3 ---------
def func_with_args(*args, **kwargs):
    print("Hi " + args[0])
    for k in kwargs:
        print(k + " => " + kwargs[k] )


#------- 4 ---------
@my_decorator_with_args
def implicit_decorator_with_args(*args, **kwargs):
    print("Hi " + args[0])
    for k in kwargs:
        print(k + " => " + kwargs[k] )

def main():
    # 1. Explicit decorator invocation
    print("\nExplicit decorator invocation")
    dec = my_decorator(func)
    dec()

    # 2. Implicit decorator invocation
    print("\nImplicit decorator invocation")
    implicit_decorator()

    # 3. Explicit decorator invocation with arguments
    print("\nExplicit decorator invocation with arguments")
    dec_with_args = my_decorator_with_args(func_with_args)
    dec_with_args("Sam", data1 = 'val1', data2 = 'val2')

    # 4. Implicit decorator invocation with arguments
    print("\nImplicit decorator invocation with arguments")
    implicit_decorator_with_args("Sam1", data11 = 'val11', data21 = 'val21')

if __name__ == '__main__':
    main()
