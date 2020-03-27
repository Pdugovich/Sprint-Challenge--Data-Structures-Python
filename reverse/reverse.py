class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # case for if no node exists
        if not node:
            return None
        # base case. If there is no next node, it has been sorted
        if node.next_node == None:
            # Still need to set the next node to the previous
            node.set_next(prev)
            # Te head will be this node
            self.head = node
            return
        else:
            # Saving a temp variable to hold the next node
            next = node.get_next()
            # reversing this node, setting next to prevous
            node.set_next(prev)
            # performing the function again on the next node
            # Which we had saved in the temp variable
            self.reverse_list(node = next, prev = node)
"""
Alright, so I see there's an input of 'prev'
but that's not given, I'll set it to None as default.

I need to check if the next_node == None, because that means
I've reached the end of the list, and it should be fully reversed,
so I can set that node to the list's head, then return

Otherwise, I need to set the next_node's next to the current node, 
then do it for the next nodes
"""
