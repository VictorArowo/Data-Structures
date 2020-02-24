import sys
sys.path.insert(
    1, '/Users/victor/Documents/python/data_structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# Stack => LIFO


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        """
        A DLL is a good choice as we are easily able to remove items from the tail of the list since we have two-way binding.
        If we had used a SLL, we would have no access to the element just before the tail from the tail.
        """

        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size
