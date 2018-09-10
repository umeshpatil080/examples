class TestDb():
    def __init__(self):
        self.id1 = "abc"

    def get_all(self, query=None, args=None, style=None, cursor=None, retry=True, **mp):
        print("**mp in get_all:")
        print(mp)
        return self._retry_transaction(self._get_all, query = query, args = args, **mp)

    def _get_all(self, query=None, args=None, style=None, cursor=None, retry=True, **mp):
            print("In get_all\nquery:{0}\nargs:{1}\nretry:{2}".format(query, args, retry))
            print("id1:" + self.id1)
            print("**mp:")
            print(mp)

            return "return_from_get_all"

    def _retry_transaction(self, _retry_def, **p):
        print("In _retry_transaction")
        print(p)
        query = p['query']
        print(_retry_def)
        return _retry_def(**p)


def main():
    query = "select * from table_name"
    args  = "args_abc"
    testdb = TestDb()
    mp = {'k1': 'v1', 'k2': 'v2'}
    result = testdb.get_all(query, args, **mp)
    print("result:" + str(result))

if __name__ == '__main__':
    main()
