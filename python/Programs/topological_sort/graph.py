import networkx as nx
from directedgraph import TestsDirectedGraph

def find_cycl(testgroup_data):
    G = TestsDirectedGraph(testgroup_data)
    try:
        #cycle_edges = nx.find_cycle(G.graph, orientation='original')
        cycle_edges = G.find_cycle()
        print("cycle_found:")
        print(cycle_edges)
        pass
    except Exception as ex:
        print("Error:" + str(ex))

def main():
    test0 = {'name': 'test0', 'runafter': []}
    test1 = {'name': 'test1', 'runafter': ['test0']}
    test2 = {'name': 'test2', 'runafter': ['test0', 'test1']}
    tests = [test0, test1, test2]

    testgroup = {'tests': tests, 'name': 'abc_testgroup'}

    find_cycl(testgroup)
    #print(testgroup)

if __name__ == '__main__':
    main()
