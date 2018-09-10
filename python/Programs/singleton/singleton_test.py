import sys
from multiprocessing import Pool, Lock, Process
from singleton import Singleton

class Log():
    def __init__(self):
        self._pid = os.getpid()

    def get_pid(self):
        return self._pid

#class TestSingletonClass(metaclass = Singleton):
class TestSingletonClass():
    def __init__(self):
        pass

    def _before_instantiating(self):
        print("In TestSingleton's method")

    def _dummy_process(self):
        obj2 = TestSingletonClass()

    def test_logging(self):
        print("In parent")
        procs = []
        func = self._dummy_process
        for i in range(2):
            p = Process(target=func)
            p.start()
            procs.append(p)
        for p in procs:
            p.join()


def main():
    t = TestSingletonClass()
    print(t.__dict__)
    t.test_logging()
    #t.super._log("from parent process")

if __name__ == '__main__':
    main()
