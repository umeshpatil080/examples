from multiprocessing import Process
import os

def info(title):
    msg = "Title:{0}".format(title)
    msg += "\nmodule name:{0}".format(__name__)
    msg += "\nparent process id:{0}".format(os.getppid())
    msg += "\nprocess id:{0}".format(os.getpid())
    print(msg)
    _log(msg, "info.txt")


def _log(msg, file):
    with open(file, 'a') as fh:
        fh.write(msg)

if(__name__ == '__main__'):
    print("In Main")
    p = Process(target = info, args = ('title_name',))
    p.start()
    p.join()