"""
Use __new__ when you need to control the creation of a new instance.
Use __init__ when you need to control initialization of a new instance.

__new__ is the first step of instance creation. It's called first, and is
responsible for returning a new instance of your class. In contrast, __init__
doesn't return anything; it's only responsible for initializing the instance
after it's been created.

"""
class Sam():
    def __new__(cls, *args, **kwargs):
        print("\nIn __new__\n")
        print("cls:")
        print(cls)
        return super(Sam, cls).__new__(cls, *args, **kwargs)
        pass

    def __init__(self):
        print("\nIn __init__\n")
        pass

    def __call__(self):
        print("\nIn __call__\n")
        print(self)
        pass

def main():
    sam = Sam()
    print(sam)
    sam()

if __name__ == '__main__':
    main()
