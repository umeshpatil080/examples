import os

class SomeResource():
     def print_data(self):
        data = "abc"
        print("\ndata:{0}".format(data))
        raise Exception("Raising explicit exception")

class RedirectStdStreams():
    def __init__(self) :
        print("\nIn __init__")

    def __enter__(self):
        print("\nIn __enter__")
        self._some_res = SomeResource()
        return self._some_res

    def __exit__(self, exc_type, exc_value, traceback):
        print("\nIn __exit__\nCleanup goes here")

        # Cleanup resource
        del(self._some_res)

        # This is important. Return True indicates
        # that we are taking care of any error and
        # clean up is being done here
        return True



def main():
    with RedirectStdStreams() as obj:
        obj.print_data()

if __name__ == '__main__':
    main()
