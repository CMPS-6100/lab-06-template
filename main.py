"""
CMPS 6100  Lab 7
Author:
"""

from my_queue import Queue
from bst import BST

def breadth_first_search(graph, source):
    visited = set()
    frontier = Queue() # use ops `append` and `popleft`
    frontier.push(source)
    while len(frontier) > 0:
        v = frontier.poll()
        if v in visited:
            continue
        
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                frontier.push(neighbor)
        
    return visited

def bfs_distances(graph, source):
    """
    bfs_distances is a modified version of breadth first 
    search. It traverses the graph in the same order as
    BFS starting from the source and keeps track of the distances
    from each vertex to the source.

    Params:
        graph.....the graph to run BFS on
        source ...the vertex to start BFS from

    Returns:
        A dictionary containing a key for every vertex in the
        graph whose value is the distance from that vertex to
        the source. The source is distance 0 away from itself.
    """
    visited = set()
    distances = {}
    frontier = Queue() # use ops `push` and `poll`
    # TO-DO
    # Implement this
    pass

def connected_components(graph):
    """
    Return the connected components in this graph.

    Params:
        graph.....the graph whose connected components will
        be returned

    Returns:
        A list of sets where each set is one of the connected
        components in the graph
    """
    # TO-DO
    # Implement this
    pass

def num_connected_components(graph):
    """
    Return the number of connected components in this graph.

    Params:
        graph.....the graph whose connected components will
        be counted

    Returns:
        The number of connected components in the graph
    """
    # TO-DO
    # Implement this
    pass
