#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     29/09/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
If a function contains at least one yield statement (it may contain other yield or return statements),
it becomes a generator function. Both yield and return will return some value from a function.

Here is how a generator function differs from a normal function.

Generator function contains one or more yield statement.
When called, it returns an object (iterator) but does not start execution immediately.
Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
Once the function yields, the function is paused and the control is transferred to the caller.
Local variables and their states are remembered between successive calls.
Finally, when the function terminates, StopIteration is raised automatically on further calls.

"""

def get_squared_sequence_detailed_upto_3():
    upperLimit = 3

    # yield actually returns an iteraton object.
    # we can execute iterator by using next(itr_obj)

    n = 1
    yield n ** 2

    n += 1
    yield n ** 2

    n += 1
    yield n** 2

def get_squared_sequence(upperLimit = 0):
    n = 0
    while(n <= upperLimit):
        yield n ** 2
        n += 1

def main():
    print("Detailed generator sequence")
    for s in get_squared_sequence_detailed_upto_3():
        print(s)

    print("Sequence from compact generator")
    for s in get_squared_sequence(5):
        print(s)

    print("Explicit genrator invocation")
    my_itr = get_squared_sequence(2)
    try:
        print(next(my_itr))
        print(next(my_itr))
        print(next(my_itr))
        print(next(my_itr))
    except StopIteration:
        print("Hit iteration upper limit")

if __name__ == '__main__':
    main()
