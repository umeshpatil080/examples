class TestCaseInfo():
    class Testcase():
        def __init__(self, nodeid, name, testcase_id):
            self._nodeid = nodeid
            self._name = name
            self._testcase_id = testcase_id

        @property
        def nodeid(self):
            return self._nodeid

        @property
        def name(self):
            return self._name

        @property
        def testcase_id(self):
            return self._testcase_id

    def __init__(self):
        self.tc_map = {}

    def add_testcase(self, nodeid = None, name = None, testcase_id = None):
        if(self.tc_map.has_key(nodeid)):
            raise "Testcase with nodeid '{}'({}) already exists in map".format(nodeid, testcase_id)
        else:
            testcase_obj = self.Testcase(nodeid, name, testcase_id)
            self.tc_map[nodeid] = testcase_obj

    def get_testcase(self, nodeid):
        if(self.tc_map.has_key(nodeid)):
            return self.tc_map[nodeid]
        else:
            None


def main():
    tcInfo = TestCaseInfo()
    tcInfo.add_testcase(nodeid = "abc::acb", name = "acb", testcase_id = 500001)
    tc = tcInfo.get_testcase(nodeid = "abc::acb")
    print(tc.testcase_id)

if __name__ == '__main__':
    main()
