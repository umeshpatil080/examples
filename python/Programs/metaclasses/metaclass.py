"""
Good read: http://blog.thedigitalcatonline.com/blog/2014/09/01/python-3-oop-part-5-metaclasses/
"""

class SingletonMetaClass(type):
    _instance = None

    def __call__(self):
        print("In __call__")
        if not self._instance:
            self._instance = super().__call__()
        return self._instance

class Sam(object, metaclass = SingletonMetaClass):

    def func(self):
        print("In func")

def main():
    # 'Sam' class object is created by 'SingletonMetaClass'.
    # 'Sam' is an object and its callable.
    # 'Sam()' calls '__call__' method of in its creator class similar to as an
    # object invokes '__call__' method in its type class.
    # In case of 'Sam' class object, 'Sam()' invokes '__call__' method in its
    # type or creator i.e ''SingletonMetaClass' class.

    # Create 1st object
    s1 = Sam()
    print("type of Sam: {0}".format(type(Sam)))
    s1.func()

    # Create 2nd object
    s2 = Sam()

    # Add an attribute s1 object. If S1 and s2 are references to same object
    # then, x can be accessed using s2 object.
    s1.x = "abc"
    print("s1: {0}\ns2: {1}\n".format(id(s1), id(s2)))
    if id(s1) == id(s2):
        print("s1 and s2 are same objects")
        print("s2.x = {0}".format(s2.x))
    else:
        print("s1 and s2 are not same objects")

if __name__ == '__main__':
    main()
