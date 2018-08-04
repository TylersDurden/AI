import queue
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def flush_q(daQ):
    while not daQ.empty():
        print("Popping: ", daQ.get())


class BinaryTree:
    def __init__(self, nodeData, left=None, right=None):
        self.value = nodeData
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def traverse(tree):
    """
    Traverse a BinaryTree
    :param tree:
    :return:
    """
    if tree.left != None:
        traverse(tree.left)
    if tree.right != None:
        traverse(tree.right)
    print(tree.value)


def q_play():
    """
    Just playing around with Queues
    :return:
    """
    daQ = queue.Queue()
    daQ.put(3)
    daQ.put(1)
    daQ.put(4)
    daQ.put(1)
    daQ.put(5)
    daQ.put(9)
    flush_q(daQ)


def create_example_binary_tree():
    """
    Makes a sample Binary Tree with a depth of 2.
    :return:
    """
    tree = BinaryTree("Root")
    BranchA = BinaryTree("Branch A")
    BranchB = BinaryTree("Branch B")
    tree.left = BranchA
    tree.right = BranchB

    LeafC = BinaryTree("Leaf C")
    LeafD = BinaryTree("Leaf D")
    LeafE = BinaryTree("Leaf E")
    LeafF = BinaryTree("Leaf F")
    LeafG = BinaryTree("Leaf G")

    BranchA.left = LeafC
    BranchA.right = LeafD
    BranchB.left = LeafE
    BranchB.right = LeafF
    traverse(tree)


def bfs(graph, start):
    """
    Simple [B]readth [F]irst [S]earch Method
    :param graph:
    :param start:
    :return:
    """
    queue = [start]
    queued = list()
    path = list()
    while queue:
        print('Queue is %s' % queue)
        vertex = queue.pop(0)
        print('Processing %s ' % vertex)
        for candidate in graph[vertex]:
            if candidate not in queued:
                queued.append(candidate)
                queue.append(candidate)
                path.append(vertex+'>'+candidate)
                print ('Adding %s to the queue' % candidate)
    return path


def dfs(graph,start):
    stack = [start]
    parents = {start:start}
    path = list()
    while stack:
        print('Stack is: %s' % stack)
        vertex = stack.pop(-1)
        print('Processing %s' % vertex)
        for candidate in graph[vertex]:
            if candidate not in parents:
                parents[candidate] = vertex
                stack.append(candidate)
                print('Adding %s to the stack' % candidate)

        path.append(parents[vertex]+'>'+vertex)
    return path[1:]


def sample_graph():
    graph = {'A': ['B', 'C'],
             'B': ['A', 'C', 'D'],
             'C': ['A', 'B', 'C', 'D', 'E'],
             'D': ['B', 'C', 'E', 'F'],
             'E': ['C', 'D', 'F'],
             'F': ['D', 'E']}
    Graph = nx.Graph()
    for node in graph:
        Graph.add_nodes_from(node)
        for edge in graph[node]:
            Graph.add_edge(node,edge)
    # Now set the x,y positions of each node
    pos = {'A': [0.00, 0.50], 'B': [0.25, 0.75],
           'C': [0.25, 0.25], 'D': [0.75, 0.75],
           'E': [0.75, 0.25], 'F': [1.00, 0.50]}
    nx.draw(Graph,pos,with_labels=True)
    nx.draw_networkx(Graph, pos)
    plt.show()
    return Graph


def sample_weighted_graph():
    """
    Display a simple example of a weighted graph
    using the Networkx library. This graph is the same
    as the one generated in sample_graph(), only with
    weighted edges.
    :return:
    """
    graph = {'A': {'B': 2, 'C': 3},
             'B': {'A': 2, 'C': 2, 'D': 2},
             'C': {'A': 3, 'B': 2, 'D': 3, 'E': 2},
             'D': {'B': 2, 'C': 3, 'E': 1, 'F': 3},
             'E': {'C': 2, 'D': 1, 'F': 1},
             'F': {'D': 3, 'E': 1}}
    Graph = nx.Graph()
    for node in Graph:
        Graph.add_nodes_from(node)
        for edge, weight in graph[node].items():
            Graph.add_edge(node, edge, weight=weight)

    # Now set the x,y positions of each node
    pos = {'A': [0.00, 0.50], 'B': [0.25, 0.75],
           'C': [0.25, 0.25], 'D': [0.75, 0.75],
           'E': [0.75, 0.25], 'F': [1.00, 0.50]}

    labels = nx.get_edge_attributes(Graph, 'weight')
    nx.draw(Graph, pos, with_labels=True)
    #nx.draw_networkx_edge_labels(Graph, pos, edge_labels=labels)
    nx.draw_networkx(Graph, pos)
    plt.show()


def algorithms_demo():
    """
    Just a demo of some basic algorithms and structures
    for traversing netwworked data.
    :return:
    """
    print "|----||----||----|ALGORITHMS_DEMO|----||----||----|"
    print "Binary Tree Example:"
    create_example_binary_tree()
    print "Queue Example: "
    q_play()
    print 'Creating an example graph to test search algorithms'
    graph = sample_graph()
    print('----------------------BFS---------------------------')
    bfs_steps = bfs(graph, 'A')
    print('----------------------DFS---------------------------')
    dfs_steps = dfs(graph, 'A')
    sample_weighted_graph()
    return 0


def main():
    #algorithms_demo()
    sample_weighted_graph()

if __name__ == '__main__':
    main()
