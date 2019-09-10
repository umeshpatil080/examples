"""
1. Base class of all objects is "object" class
2. A class also is an object of class type "type"

=> object is the base of every object, type is the class of every type

Metaclass-
    A metaclass is the class of a class. Like a class defines how an instance
    of the class behaves, a metaclass defines how a class behaves. A class is
    an instance of a metaclass.

    A object => is an instance of a class
    A class  => is an instance of a metaclass

    All classes by default instances of class "type". So "type" is default
    metaclass in Python.

    Creating metaclass - To create your own metaclass in Python you really
    just want to subclass type.

Metaclass good read -
https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
http://blog.thedigitalcatonline.com/blog/2014/09/01/python-3-oop-part-5-metaclasses/

"""

class Singleton(type):
    _instance = None

    # override __call__ method of parent class "type".
    # '__call__' invoked when an object is called i.e, obj().
    # So "metaclass = Singleton" executes, it instantiates
    # an object of type "Singleton" and makes a call on that
    # object which results invokation of "__call__" method.
    def __call__(self, *args, **kwargs):
        if not self._instance:
            # no object is cached, get an object using "self".
            # "self" here is an object of type "Singleton".

            # super=> get a proxy object using "Singleton" class and its object
            # which can be used call parent class methods overriden here in
            # child class. In this case its "__call__".
            # invoke parent class "type"'s __call__ method for python to finish
            # construction of object instantiated.
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
            print("Type of self:{0}".format(type(self)))
            print("Type of self._instance:{0}".format(type(self._instance)))
            print("Is self and self._instance same:{0}".format(self is self._instance))
            print("Address of self:{0}".format(id(self)))
            print("Address of self._instance:{0}".format(id(self._instance)))

        return self._instance

class SamSingleton(metaclass = Singleton):
    pass

"""
# One more way implementing singleton class with global variable

_instance = None
class SamSingleton(object):
    def __new__(cls, *args, **kwargs):
        global _instance
        if _instance is None:
            _instance = super().__new__(cls,*args, **kwargs)
        return _instance
"""

class SamTest(object):
    pass

def main():
    a = SamSingleton()
    b = SamSingleton()

    print("-----------__main__------------")
    # Here type of class "SamSingleton" has been changed to a custom type
    # using metaclass i.e, "SamSingleton" class is now instance of class
    # "Singleton" instead of being instance of class "type".
    print("Type of SamTest:{0}".format(type(SamTest))) #instance of class "type"
    print("Type of SamSingleton:{0}".format(type(SamSingleton)))
    print("Type of object a:{0}".format(type(a)))
    print("a is b: {0}".format(a is b))
    print("Object a's address: {0}".format(id(a)))
    print("Object b's address: {0}".format(id(b)))

if __name__ == '__main__':
    main()
