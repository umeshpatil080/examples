import os
from time import sleep

from nate_db import testdb_global

obj = testdb_global('parent')

def child_process():
    child_pid = os.getpid()
    print("\nchild: actual child pid: " + str(child_pid) + "\n")
    print("child: pid from cached global object: {0}\n".format(obj.get_process_id()))
    obj1 = testdb_global('child')

def main():
    pid = os.fork()
    if pid == 0:
        child_process()
        exit(0)
    else:
        p_pid = os.getpid()
        print("\nparent: parent pid: " + str(p_pid) + "\n")
        print("parent: pid from cached global object: {0}\n".format(obj.get_process_id()))

if __name__ == '__main__':
    main()