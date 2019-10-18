import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.stack = Stack()
        self.queue = Queue()

    # Insert the given value into the tree
    def insert(self, value):
        if value > self.value:
            if  not self.right:
                self.right = BinarySearchTree(value)
            else: #there is a value to the right
                self.right.insert(value)
        else: # value <= self.value
            if not self.left:
                self.left = BinarySearchTree(value)
            else: #no value ot left
                self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else: #right exists
            #go right
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
            cb(self.value)
            
            if self.left:
                self.left.for_each(cb)
            if self.right:
                self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        print(":::::::")
        # print(self.stack.size)
        self.queue.enqueue(self)
        while(self.queue.size > 0):
            node = self.queue.dequeue()
            if node.left:
                self.queue.enqueue(node.left)
            if node.right:
                self.queue.enqueue(node.right)
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(":::::::")
        # print(self.stack.size)
        self.stack.push(self)
        while(self.stack.size > 0):
            node = self.stack.pop()
            if node.left:
                self.stack.push(node.left)
            if node.right:
                self.stack.push(node.right)
            print(node.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

print("order expected\n", "1\n2\n3\n4\n5\n6\n7\n8\n")
bst.in_order_print(bst)

print("bft expected\n", "1\n8\n5\n3\n7\n2\n4\n6\n")
bst.bft_print(bst)

print("dft expected\n", "1\n8\n5\n7\n6\n3\n4\n2\n")
bst.dft_print(bst)