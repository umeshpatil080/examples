import sys

class Test(object):
    def __init__(self, name, runafter=[]):
        self.name = name
        self.runafter = runafter

def get_tests():
    tests = []
    t1 = Test('bar')
    t2 = Test('baz')
    t3 = Test('foo', ['bar', 'baz'])
    t4 = Test('hello', ['foo', 'bar'])
    tests.append(t1)
    tests.append(t2)
    tests.append(t3)
    tests.append(t4)
    return tests

def get_cyclic_tests():
    """
    A           B
    ^ \
    |  \                  E
    |   \>
    C <--D

    """
    tests = []
    t1 = Test('A', ['C'])
    t2 = Test('B')
    t3 = Test('C', ['D'])
    t4 = Test('D', ['A', 'E'])
    t5 = Test('E', ['B'])
    tests.append(t1)
    tests.append(t2)
    tests.append(t3)
    tests.append(t4)
    tests.append(t5)
    return tests

def get_cycle_tests_1():
    tests = []
    t1 = Test('A', ['D'])
    t2 = Test('B', ['E'])
    t3 = Test('C', ['A'])
    t4 = Test('D', ['B', 'C', 'E'])
    t5 = Test('E', 'A')
    tests.append(t1)
    tests.append(t2)
    tests.append(t3)
    tests.append(t4)
    tests.append(t5)
    return tests

def get_no_cycle_tests():
    tests = []
    t1 = Test('A', ['B'])
    t2 = Test('B')
    t3 = Test('C', ['A', 'D'])
    t4 = Test('D', ['A', 'E'])
    t5 = Test('E', ['B'])
    tests.append(t1)
    tests.append(t2)
    tests.append(t3)
    tests.append(t4)
    tests.append(t5)
    return tests

def get_no_cycle_tests_1():
    tests = []
    t1 = Test('A', [])
    t2 = Test('B', ['E'])
    t3 = Test('C', ['A'])
    t4 = Test('D', ['A', 'B', 'C', 'E'])
    t5 = Test('E', 'A')
    tests.append(t1)
    tests.append(t2)
    tests.append(t3)
    tests.append(t4)
    tests.append(t5)
    return tests

def get_no_cycle_tests_2():
    tests = []
    t1 = Test('A', ['B'])
    t2 = Test('B')
    t3 = Test('C', ['A'])
    t4 = Test('D', ['A', 'E'])
    t5 = Test('E', ['B'])
    tests.append(t1)
    tests.append(t2)
    tests.append(t3)
    tests.append(t4)
    tests.append(t5)
    return tests

class Node(object):
    def __init__(self, name, runafter=[]):
        self.name = name
        self.runafter = runafter
        self.indegree = 0
        self.outdegree = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def node_number(self):
        return self._node_number

    @node_number.setter
    def node_number(self, value):
        self._node_number = value

    @property
    def runafter(self):
        return self._runafter

    @runafter.setter
    def runafter(self, value):
        self._runafter = value

    @property
    def indegree(self):
        return self._indegree

    @indegree.setter
    def indegree(self, value):
        self._indegree = value

    @property
    def outdegree(self):
        return self._outdegree

    @outdegree.setter
    def outdegree(self, value):
        self._outdegree = value

class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self._nodes_count = len(self.nodes)
        self._node_name_index_map = {}
        self._index_node_map = {}
        for i in range(len(self.nodes)):
            self._node_name_index_map[self.nodes[i].name] = i
            self._index_node_map[i] = self.nodes[i]

    @property
    def nodes_count(self):
        return self._nodes_count

    @property
    def node_name_index_map(self):
        return self._node_name_index_map

    @property
    def index_node_map(self):
        return self._index_node_map

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, value):
        self._nodes = value

    def build_graph(self):
        rows_count = col_count = len(self.nodes)
        self.g = [[0 for j in range(col_count)] for i in range(rows_count)]

        # construct directed graph
        for node in self.nodes:
            if len(node.runafter) > 0:
                dest_node_index = self.node_name_index_map[node.name]
                for runafter_node_name in node.runafter:
                    src_node_index = self.node_name_index_map[runafter_node_name]

                    # There is path from 'src_node_index' to 'dest_node_index'
                    self.g[src_node_index][dest_node_index] = 1

                    # Update outdegree and indegree for nodes
                    self.nodes[src_node_index].outdegree += 1
                    self.nodes[dest_node_index].indegree += 1

        return self.g

    def topological_order(self):
        if self.is_DAG():
            indegree = {}
            for node in self.nodes:
                indegree[node.name] = node.indegree

            visted_nodes = {}
            topologically_sorted_nodes = []
            while(len(indegree)):
                for node_name in list(indegree.keys()):
                    if node_name in visted_nodes:
                        continue

                    # get a not visited node with 0 indegree
                    if indegree[node_name] == 0:
                        # mark node as visited and remove from indegree
                        # collection to avoid further processing
                        visted_nodes[node_name] = True
                        indegree.pop(node_name)
                        topologically_sorted_nodes.append(node_name)

                        # decrease indegree of adjacent node reachable
                        # from 'node' being processed
                        node_index = self.node_name_index_map[node_name]
                        for adj_node_index in range(self.nodes_count):
                            if self.g[node_index][adj_node_index] == 1:
                                adj_node_name = self.index_node_map[adj_node_index].name
                                indegree[adj_node_name] -= 1
        else:
            raise Exception("Cycle found.")

        return topologically_sorted_nodes

    def find_exec_order(self, exclude_nodes=[]):
        """
        Modified topological order -
            1. Group nodes with zero indegrees
            2. Store node group in an array 'topologically_sorted_nodes_group'
            3. Update indegrees of other non-visited nodes
            4. Repeat step #1 to #3 until all nodes are visted
            5. 'topologically_sorted_nodes_group' array gives execution order
        """
        if self.is_DAG():
            indegree = {}
            for node in self.nodes:
                indegree[node.name] = node.indegree

            # Remove nodes specified in 'exclude_nodes'
            # Update indegree dependency of adjacent nodes
            for executed_node_name in exclude_nodes:
                indegree.pop(executed_node_name)
                executed_node_index = self.node_name_index_map[executed_node_name]
                for adj_node_index in range(self.nodes_count):
                    if self.g[executed_node_index][adj_node_index] == 1:
                        adj_node_name = self.index_node_map[adj_node_index].name
                        indegree[adj_node_name] -= 1

            topologically_sorted_nodes_group = []
            while(len(indegree)):
                no_dependency_nodes = []
                for node_name in list(indegree.keys()):
                    node_indegree = indegree[node_name]
                    if node_indegree == 0:
                        no_dependency_nodes.append(node_name)
                        indegree.pop(node_name)

                topologically_sorted_nodes_group.append(no_dependency_nodes)

                # decrease indegree of adjacent node reachable from
                # 'node' being processed to yield next node to execute
                for visited_node_name in no_dependency_nodes:
                    visited_node_index = self.node_name_index_map[visited_node_name]
                    for adj_node_index in range(self.nodes_count):
                        if self.g[visited_node_index][adj_node_index] == 1:
                            adj_node_name = self.index_node_map[adj_node_index].name
                            indegree[adj_node_name] -= 1
        else:
            raise Exception("Cycle found")

        return topologically_sorted_nodes_group

    def is_DAG(self):
        for start_node in self.nodes:
            cycle_candidate_nodes = []
            if start_node.indegree > 0 and start_node.outdegree > 0:
                prev_node = start_node
                while(True):
                    # get all nodes adjacent to 'node'
                    prev_node_index = self.node_name_index_map[prev_node.name]
                    for adj_node_index in range(self.nodes_count):
                        # is there path from 'node' to 'adj_node'
                        if self.g[prev_node_index][adj_node_index] == 1:
                            adj_node = self.index_node_map[adj_node_index]
                            cycle_candidate_nodes.append(adj_node)

                    no_of_candidate_nodes = len(cycle_candidate_nodes)
                    if no_of_candidate_nodes == 0:
                        break

                    next_node = cycle_candidate_nodes.pop(0)
                    if next_node.name == start_node.name:
                        return False
                    prev_node = next_node
                break
        return True

    def _isCyclic(self, node_num, visited, recStack, cycle_nodes):
        # Mark current node as visited and
        # adds to recursion stack
        visited[node_num] = True
        recStack[node_num] = True
        cycle_nodes.append(node_num)

        # Visist all adjacent nodes in DFS manner.
        # If any adjacent node is visited and in
        # recStack then graph is cyclic
        for adj_node_num in range(self.nodes_count):
            if self.g[node_num][adj_node_num] == 1:
                if visited[adj_node_num] == False:
                    if self._isCyclic(adj_node_num, visited, recStack, cycle_nodes) == True:
                        return True
                elif recStack[adj_node_num] == True:
                    return True

        # The node 'node_num' does not result in cycle.
        # The node needs to be poped from
        # recursion stack before function ends
        recStack[node_num] = False
        cycle_nodes.pop()
        return False

    def isCyclic(self):
        visited = [False] * self.nodes_count
        recStack = [False] * self.nodes_count

        cycle_nodes = []
        for node_num in range(self.nodes_count):
            if visited[node_num] == False:
                if self._isCyclic(node_num, visited, recStack, cycle_nodes) == True:
                    sys.stdout.write("cycle_nodes:")
                    for node_index in cycle_nodes:
                        sys.stdout.write(self.index_node_map[node_index].name + " ->")
                    sys.stdout.write(self.index_node_map[node_num].name + "\n")
                    return True
        return False

    def print_node_degrees(self):
        print("\n{0:10}{1:10}{2:10}".format('Node', 'Indegree', 'Outdegree'))
        for node in self.nodes:
            print("{0:10}{1:5}{2:10}".format(node.name, node.indegree, node.outdegree))

    def print_graph(self):
        if self.g:
            for row in self.g:
                for c in row:
                    sys.stdout.write("{0}\t".format(c))
                sys.stdout.write("\n")

def get_nodes(tests):
    nodes = []
    for test in tests:
        node = Node(test.name, test.runafter)
        nodes.append(node)
    return nodes

def main():
    try:
        #tests = get_no_cycle_tests()
        #tests = get_no_cycle_tests_1()

        #tests = get_no_cycle_tests_2()
        tests = get_cyclic_tests()

        nodes = get_nodes(tests)
        tc_order = Graph(nodes)
        tc_order.build_graph()

        tc_order.print_graph()
        tc_order.print_node_degrees()

        is_dag = tc_order.is_DAG()
        print("\nIs DAG: {0}".format(is_dag))

        is_cyclic = tc_order.isCyclic()
        print("is_cyclic: {0}".format(is_cyclic))

        print("\ntopological_order:")
        print(tc_order.topological_order())

        print("\nfind_exec_order:")
        print(tc_order.find_exec_order())
    except Exception as ex:
        print("Error:" + str(ex))

if __name__ == '__main__':
    main()
