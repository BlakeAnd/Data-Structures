from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        self.size -= 1
        self.storage.remove_from_item()

    def len(self):
        pass
