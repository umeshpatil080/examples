import networkx as nx


class TestsDirectedGraph():
    def __init__(self, testgroup_data):
        if 'tests' not in testgroup_data:
            raise Exception("Missing tests data")

        self.graph = nx.DiGraph()
        self.group_name = testgroup_data['name']
        self.tests = testgroup_data['tests']
        self.nodes_count = len(self.tests)
        self.node_name_index_map = self.tests
        self._build_graph()

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, value):
        self._graph = value

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value

    @property
    def tests (self):
        return self._tests

    @tests.setter
    def tests(self, value):
        self._tests = value

    @property
    def nodes_count(self):
        return self._nodes_count

    @nodes_count.setter
    def nodes_count(self, value):
        self._nodes_count = value

    @property
    def node_index_name_map(self):
        return self._node_index_name_map

    @property
    def node_name_index_map(self):
        return self._node_name_index_map

    @node_name_index_map.setter
    def node_name_index_map(self, value):
        self._node_name_index_map = {}
        self._node_index_name_map = {}
        for i in range(self.nodes_count):
            test_name = value[i]['name']
            if test_name not in self._node_name_index_map:
                self._node_name_index_map[test_name] = i
                self._node_index_name_map[i] = test_name
            else:
                raise Exception("Duplicate testcase '{0}' found in testgroup '{1}'.".format(test_name, self.group_name))

    def _build_graph(self):
        for test in self.tests:
            test_name = test['name']
            if 'runafter' in test:
                runafter_map = {}
                test_index = self.node_name_index_map[test_name]
                for runafter_test in test['runafter']:
                    if runafter_test not in runafter_map:
                        if runafter_test in self.node_name_index_map:
                            runafter_map[runafter_test] = True
                            runafter_test_index = self.node_name_index_map[runafter_test]

                            # Here 'test' should execute after 'runafter_test'.
                            # So 'test' is dependent on 'runafter_test'.
                            # Add an edge from 'runafter_test' to 'test' indicating
                            # that 'runafter_test' comes before 'test' in topological order.
                            self.graph.add_edge(runafter_test_index, test_index)
                        else:
                            raise Exception("runafter test '{0}' of testcase '{1}' does not exist in " \
                            "testgroup '{2}'.\nTests in testgroup '{2}' are: {3}"
                            .format(runafter_test, test_name, self.group_name, ",".join(list(self.node_name_index_map.keys()))))
                    else:
                        raise Exception("'{0}' runafter test appears more than " \
                        "once for testcase '{1}' in testgroup '{2}'. Runafter tests are: {3}" \
                        .format(runafter_test, test_name, self.group_name, ",".join(test['runafter'])))
            else:
                  pass

    def find_cycle(self):
        cycle_edges = []
        try:
            # orientation='original' - every edge is treated as directed
            cycle_edges = nx.find_cycle(self.graph, orientation='original')
            # Cycle found
        except Exception as ex:
            # No cycle found
            pass

        return cycle_edges


if __name__ == "__main__":
    pass