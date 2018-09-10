class TestDb():
    def __init__(self):
        self.id1 = "abc"

    def get_all(self, query=None, args=None, style=None, cursor=None, retry=True, **kwargs):
        return self._execute_transaction(self._get_all, target = '_get_all', query = query, args = args, **kwargs)

    def _get_all(self, query=None, args=None, style=None, cursor=None, retry=True, **kwargs):
            print("In _get_all\tquery:{0}\targs:{1}\tretry:{2}".format(query, args, retry))
            print("id1:" + self.id1)
            print("kwargs:{0}".format(kwargs))

            return "return_from_get_all"

    def get_one(self, query = None, args = None, **kwargs):
        return self._execute_transaction(self._get_one, query = query, args = args, target = "_get_one", **kwargs)

    def _get_one(self, query = None, args = None, **kwargs):
        print("In _get_one\tquery:{0}\targs:{1}\tkwargs:{2}".format(query, args, kwargs))
        return "data from _get_one"

    def _execute_transaction(self, _retry_def, **kwargs):
        target = kwargs['target']
        query = kwargs['query']
        try:
            print("##################### Begin: In _execute_transaction executing '{0}' #####################".format(target))
            val = _retry_def(**kwargs)
            print("##################### End  : In _execute_transaction executing '{0}' #####################".format(target))
            return val
        except Exception as e:
            print("Common exception handling")


def main():
    query = "select * from table_name"
    args  = "args_abc"
    testdb = TestDb()
    mp = {'k1': 'v1', 'k2': 'v2'}
    result = testdb.get_all(query, args, **mp)
    print("result:" + str(result))

    kwargs = {'k11' : 'v11'}
    result = testdb.get_one("select * from t limit 1", "arg1", **kwargs)
    print(result)

if __name__ == '__main__':
    main()
