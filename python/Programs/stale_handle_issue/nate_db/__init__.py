import os

from .natedb import TestDB

_Global = None
_pid = os.getpid()

def testdb_global(context):
    global _Global
    global _pid

    if _Global:
        print("\n{0}: _Global is defined - Returning cached object\n".format(context))
        if _pid != os.getpid():
            print("{0}: Warning - '_Global' object instantiating process is different than current one. Need to re-construct object.\n".format(context))
        return _Global
    else:
        _Global = TestDB()
        print("{0}: _Global is not defined - Instantiating new object\n".format(context))
        return _Global