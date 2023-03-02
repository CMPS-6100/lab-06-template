import random
from my_queue import Queue
from bst import BST
from main import bfs_distances, connected_components, num_connected_components

##################################################
##                    BST Tests                 ##
##################################################

def test_bst_create_tree():
    bst = BST(7)
    assert bst.element == 7
    assert bst.left == None
    assert bst.right == None

def build_tree(lst):
    bst = BST(lst[0])
    for element in lst[1:]:
        bst.insert(element)
    return bst

def test_bst_insert_second_level():
    # Insert 7, 3, 13
    # Verify Tree is
    #       7
    #     /    \
    #    3      13
    bst = BST(7)
    bst.insert(3)
    bst.insert(13)
    l = bst.left
    r = bst.right
    assert bst.element == 7
    assert l.element == 3
    assert l.left == None
    assert l.right == None
    assert r.element == 13
    assert r.left == None
    assert r.right == None

def test_bst_insert_third_level():
    # Insert [7, 3, 13, 2, 5, 11, 17]
    # Verify Tree is
    #       7
    #     /    \
    #    3      13
    #   / \    /  \
    #  2   5  11  17
    elements = [7, 3, 13, 2, 5, 11, 17]
    bst = build_tree(elements)

    three_left = bst.left.left
    three_right = bst.left.right
    thirteen_left = bst.right.left
    thirteen_right = bst.right.right

    assert three_left.element == 2
    assert three_left.left == None
    assert three_left.right == None
    assert three_right.element == 5
    assert three_right.left == None
    assert three_right.right == None
    assert thirteen_left.element == 11
    assert thirteen_left.left == None
    assert thirteen_left.right == None
    assert thirteen_right.element == 17
    assert thirteen_right.left == None
    assert thirteen_right.right == None

def test_bst_contains():
    # Run contains on
    #       11
    #     /    \
    #    5      17
    #   / \    /  \
    #  3   7  13  19
    elements = [11, 5, 17, 3, 7, 13, 19]
    bst = build_tree(elements)
    assert bst.contains(11)
    assert bst.contains(5)
    assert bst.contains(17)
    assert bst.contains(3)
    assert bst.contains(7)
    assert bst.contains(13)
    assert bst.contains(19)
    assert not bst.contains(2)
    assert not bst.contains(4)
    assert not bst.contains(6)
    assert not bst.contains(8)
    assert not bst.contains(12)
    assert not bst.contains(14)
    assert not bst.contains(18)
    assert not bst.contains(20)

def test_traverse_preorder_1():
    # Run preorder traverse on
    #       11
    #     /    \
    #    5      17
    #   / \    /  \
    #  3   7  13  19
    elements = [11, 5, 17, 3, 7, 13, 19]
    bst = build_tree(elements)

    actual = []
    bst.traverse_preorder(actual)
    assert actual == [11, 5, 3, 7, 17, 13, 19]

def test_traverse_preorder_2():
    # Run preorder traverse on
    #       15
    #     /    \
    #    5      17
    #     \    /  \
    #      7  16  19
    elements = [15, 5, 17, 7, 16, 19]
    bst = build_tree(elements)

    actual = []
    bst.traverse_preorder(actual)
    assert actual == [15, 5, 7, 17, 16, 19]

def test_traverse_inorder():
    # Run inorder traverse on
    #       11
    #     /    \
    #    5      17
    #   / \    /  \
    #  3   7  13  19
    elements = [11, 5, 17, 3, 7, 13, 19]
    bst = build_tree(elements)

    actual = []
    bst.traverse_inorder(actual)
    assert actual == [3, 5, 7, 11, 13, 17, 19]

def test_traverse_inorder_random():
    # Run inorder traverse of a randomly
    # generated tree containing elements
    # 0-99
    elements = [i for i in range(100)]
    expected = list(elements)
    random.shuffle(elements)
    bst = build_tree(elements)
    actual = []
    bst.traverse_inorder(actual)
    assert actual == expected

def test_traverse_postorder_1():
    # Run postorder traverse on
    #       11
    #     /    \
    #    5      17
    #   / \    /  \
    #  3   7  13  19
    elements = [11, 5, 17, 3, 7, 13, 19]
    bst = build_tree(elements)

    actual = []
    bst.traverse_postorder(actual)
    assert actual == [3, 7, 5, 13, 19, 17, 11]

def test_traverse_postorder_2():
    # Run preorder traverse on
    #       15
    #     /    \
    #    5      17
    #     \    /  \
    #      7  16  19
    elements = [15, 5, 17, 7, 16, 19]
    bst = build_tree(elements)

    actual = []
    bst.traverse_postorder(actual)
    assert actual == [7, 5, 16, 19, 17, 15]

##################################################
##                   Queue Tests                ##
##################################################

def test_queue():
    q = Queue()
    q.push(1)
    assert q.peek() == 1
    q.push(2)
    assert q.peek() == 1
    q.push(3)
    assert q.peek() == 1
    assert q.poll() == 1
    assert q.poll() == 2
    assert q.poll() == 3
    assert q.is_empty()

##################################################
##               BFS Distance Tests             ##
##################################################

def test_bfs_distances_simple():
    # trivial graph with only two vertices
    graph = {
            'A': ['B'],
            'B': ['A']
        }
    distances = bfs_distances(graph,'A')
    assert distances['A'] == 0
    assert distances['B'] == 1
    
def test_bfs_distances_triangle():
    # trivial graph with only two vertices
    graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B']
        }
    distances = bfs_distances(graph,'A')
    assert distances['A'] == 0
    assert distances['B'] == 1
    assert distances['C'] == 1

def test_bfs_distances_full():
    # same as animated example from notes
    graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B'],
            'E': ['B', 'H'],
            'F': ['C'],
            'G': ['C'],
            'H': ['E']
        }
    distances = bfs_distances(graph, 'A')
    assert distances['A'] == 0
    assert distances['B'] == 1
    assert distances['C'] == 1
    assert distances['D'] == 2
    assert distances['E'] == 2
    assert distances['F'] == 2
    assert distances['G'] == 2
    assert distances['H'] == 3

##################################################
##             Connected Components             ##
##################################################

def test_connected_components_one():
    graph = {
            'A': ['B'],
            'B': ['A'],
        }

    components = connected_components(graph)
    assert len(components) == 1
    assert components[0] == {'A', 'B'}

def test_connected_components_two():
    graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C']
        }
    components = connected_components(graph)
    assert len(components) == 2
    assert components[0] == {'A', 'B'}
    assert components[1] == {'C', 'D'}

def test_connected_components_three():
    graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F', 'G'],
            'F': ['E', 'G'],
            'G': ['E', 'F'],
        }
    components = connected_components(graph)
    assert len(components) == 3
    assert components[0] == {'A', 'B'}
    assert components[1] == {'C', 'D'}
    assert components[2] == {'E', 'F', 'G'}

def test_num_connected_components():
    graph = {
            'A': ['B'],
            'B': ['A'],
        }
    assert num_connected_components(graph) == 1
    graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C']
        }
    assert num_connected_components(graph) == 2
    graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F', 'G'],
            'F': ['E', 'G'],
            'G': ['E', 'F'],
        }
    assert num_connected_components(graph) == 3