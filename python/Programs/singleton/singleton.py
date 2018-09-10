import os

class Singleton(type):
    def __init__(self, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        self._instance = None
        self._pid = os.getpid()

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            #msg = "current pid:{0}\tself.id:{1}\tNeed to release resources inherited from parent\n".format(os.getpid(), self._pid)
            #print(msg)
            #self._log(msg)
            pass

        if os.getpid() != self._pid:
            msg = "current pid:{0}\tself.id:{1}\tNeed to release resources inherited from parent\n".format(os.getpid(), self._pid)
            print(msg)
            self._log(msg)
        self._before_instantiating(super)
        self._instance = super().__call__(*args, **kwargs)
        # update the pid
        self._pid = os.getpid()
        return self._instance

    def _before_instantiating(self, super=None):
        print("In {0}::_before_instantiating".format(type(self).__name__))

    def _log(self, msg):
        filename = 'C:\DATA_\Reading Material\Python\Programs\singleton\sam.log'
        with open(filename, 'a+') as fh:
            fh.write(msg)