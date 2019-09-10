import os

from .natedb import TestDB

_Global = None
_pid = os.getpid()

def testdb_global(context):
    global _Global
    global _pid

    if _Global:
        print("{0}: _Global is defined - Returning cached object".format(context))
        if _pid != os.getpid():
            print("{0}: Warning - Process that instantiated '_Global' object is different. " \
                  "Need to re-construct object.\n".format(context))
            # fix would be re-instantiating TestDB() and updating _Global
            # _Global = TestDB()
        return _Global
    else:
        _Global = TestDB()
        print("{0}: _Global is not defined - Instantiating new object".format(context))
        return _Global