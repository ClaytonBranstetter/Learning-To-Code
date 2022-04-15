class Node:
    def __init__(self , value=0, next_node=None):
            """Initialize node"""
            self.value = value
            self.next = next_node

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, entry):
        """Put the entry at the top of the Stack."""
        node = Node(entry)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def is_empty(self):
        """Return True if Stack is empty, False otherwise."""
        return self.length == 0

    def peek(self):
        """Return value at the top of the Stack, raise a RuntimeError otherwise."""
        if self.is_empty():
            raise RuntimeError
        return self.head.value

    def pop(self):
        """Remove and return the value at the top of the stack. Raise RuntimeError otherwise."""
        if self.is_empty():
            raise RuntimeError
        self.head = self.head.next
        self.length -= 1

class Queue:
    def __init__(self):
        self.head = None
        self.length = 0

    def enqueue(self, entry):
        """Put the entry at the back of the Queue."""
        new_node = Node(entry)
        if self.head is None:
           self.head = new_node
           self.next = self.head
        else:
           self.next.next = new_node
           self.next = new_node
        self.length += 1

    def is_empty(self):
        """Return True if Queue is empty, False otherwise."""
        return self.length == 0

    def peek_front(self):
        """Return value at the front of the queue, raise a RuntimeError otherwise."""
        if self.is_empty():
            raise RuntimeError
        head = self.head
        return head.value

    def dequeue(self):
        """Remove and return the value at the front of the Queue. Raise RuntimeError otherwise."""
        if self.is_empty():
            raise RuntimeError
        self.head = self.head.next
        self.length -= 1

class LinkedList:
    def __init__(self, head = None):
        """Initialize list"""
        self.head = head
        self.length = 0
    
    def length(self):
        """Return length of the list"""
        return self.length
    
    def insert(self, index, entry):
        """Insert the entry at the index. Valid indices range from 0 to length inclusively.
        Inserting at index=0 inserts at the front. Inserting at index=length adds to the back.
        Each insert increases the length by 1."""
        if index < 0 or index > self.length:
            raise RuntimeError
        if index == 0:
            self.head = Node(entry, self.head)
        else:
            node = self.head
            for _ in range(index-1):
                node = node.next
            node.next = Node(entry, node.next)
        self.length += 1

    def remove(self, index):
        """Removes the entry at the index. Valid indices range from 0 to length-1 inclusively.
        Each remove decreases the length by 1."""
        if index < 0 or index >= self.length:
            raise RuntimeError
        if index == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(index):
                if node.next and node.next.next:
                    node = node.next
            node.next = node.next.next
        self.length -= 1

    def get_entry(self, index):
        """Return the entry at index, raises a RuntimeError otherwise."""
        if index < 0 or index >= self.length:
            raise RuntimeError
        node = self.head
        for _ in range(index):
            node = node.next
        return node.value

    def set_entry(self, index, entry):
        """Sets the entry at index, raises a RuntimeError otherwise. Even if successful, the length remains the same."""
        if index < 0 or index >= self.length:
            raise RuntimeError
        node = self.head
        for _ in range(index):
            node = node.next
        node.value = entry

    def clear(self):
        """Empties the list"""
        self.head = None
        self.length = 0

    def reverse(self):
        for i in range(self.length):
            last_index = self.length-1
            last_element = self.get_entry(last_index)
            self.remove(last_index)
            self.insert(i, last_element)
