"""
CMPS 6100  Lab 6
Author:
"""

class BST:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
    
    def insert(self, element):
        # done
        if element < self.element:
            # if the element belongs in the left subtree,
            # but there is nothing there, put this element there
            if self.left == None:
                self.left = BST(element)
            else:
                # recursively insert into the left subtree
                self.left.insert(element)
        else:
            # if the element belongs in the right subtree,
            # but there is nothing there, put this element there
            if self.right == None:
                self.right = BST(element)
            else:
                # recursively insert into the right subtree
                self.right.insert(element)

    def contains(self, key):
        # done
        if key < self.element:
            # if we should go left, but there is no
            # left subtree, key not in tree
            if self.left == None:
                return False
            # continue search in left subtree
            return self.left.contains(key)
        elif key > self.element:
            # if we should go right, but there is no
            # right subtree, key not in tree
            if self.right == None:
                return False
            # continue search in left subtree
            return self.right.contains(key)
        else:
            # if the key isn't less than or greater than
            # self.element, it is equal to it!
            return True
        
    def traverse_preorder(self, lst):
        # TO-DO
        # Implement this
        # append every element in this tree to lst
        # as they are visited by this traveral
        pass

    def traverse_inorder(self, lst):
        # TO-DO
        # Implement this
        # append every element in this tree to lst
        # as they are visited by this traveral
        pass

    def traverse_postorder(self, lst):
        # TO-DO
        # Implement this
        # append every element in this tree to lst
        # as they are visited by this traveral
        pass