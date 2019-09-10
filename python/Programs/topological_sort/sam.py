import networkx as nx
from networkx.exception import NetworkXNoCycle

def sam():
    #G = nx.DiGraph([(0, 1), (2,1), (1, 2)])
    G = nx.DiGraph()
    G.add_edge('A', 'B')
    G.add_edge('B','C')
    G.add_edge('C', 'D')
    try:
        cycle_edges = nx.find_cycle(G, orientation='original')
        print("cycle_found:")
        print(cycle_edges)
    except NetworkXNoCycle as ex:
        print("Error:" + str(ex))

def main():
    sam()


if __name__ == '__main__':
    main()
