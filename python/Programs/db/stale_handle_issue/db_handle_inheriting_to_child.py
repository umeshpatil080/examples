import os
from time import sleep

from nate_db import testdb_global

"""
Purpose of this code is to demonstrate that objects created in
parent get copied to child when a child process is created via fork.

This may create stale stale db, file hadlers in child process and result
in unexpected child behaviour like child process gettinh hung infinately.
"""


# This is in parent address space. When testdb_global()
# first time invoked it creates an object of type TestDB.
# Here testdb_global() method acts like sigleton object creator.
obj = testdb_global('parent')

def child_process():
    # Child process also gets 'obj' TestDB object from parent which
    # will be having stale data. If its class type handle db or file
    # operations then, it may create problems. So in child we need to
    # handle cleaning-up of stale hadles inherited from parent process
    # and re-instantiating again in child if required.
    child_pid = os.getpid()
    print("child: actual child pid: " + str(child_pid)) # this gives us the actual pid
    print("child: pid from cached global object: {0}\n".format(obj.get_process_id())) # this gives stale pid value inhirted from parent

    # This may return stale TestDB object if not handled correct in 'testdb_global'.
    # Currently it returns stale object. Current pid and cached pid can be used to
    # get refreshed TestDB object.
    obj1 = testdb_global('child')

def main():
    pid = os.fork()
    if pid == 0:
        # In child process
        child_process()
        exit(0)
    else:
        # In parent process
        p_pid = os.getpid()
        print("parent: parent pid: " + str(p_pid))
        print("parent: pid from cached global object: {0}\n".format(obj.get_process_id()))

if __name__ == '__main__':
    main()