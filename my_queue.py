"""
CMPS 6100  Lab 6
Author:
"""

from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def __len__(self):
        return self.queue.size
    
    def is_empty(self):
        return len(self) == 0

    def push(self, element):
        # TO-DO
        # Implement this
        pass

    def poll(self):
        # TO-DO
        # Implement this
        pass

    def peek(self):
        # TO-DO
        # Implement this
        pass