'''
Author: Clayton Branstetter
KUID: 3089206
Date: 03/04/2022
Lab: lab#04
Last modified: 03/11/2022
Purpose: Web History Simulator
'''


class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        """ Initialize list """
        self.head = head
        self.length = 0

    def length(self):
        """ Return length of the list """
        return self.length

    def insert(self, index, entry):
        """ Insert the entry at the index. Valid indices range from 0 to length inclusively.
        Inserting at index=0 inserts at the front. Inserting at index=length adds to the back.
        Each insert increases the length by 1. """
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
        """ Removes the entry at the index. Valid indices range from 0 to length-1 inclusively.
        Each remove decreases the length by 1. """
        if index < 0 or index >= self.length:
            raise RuntimeError
        if index == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(index):
                node = node.next
            node.next = node.next.next
        self.length -= 1

    def get_entry(self, index):
        """ Return the entry at index, raises a RuntimeError otherwise. """
        if index < 0 or index >= self.length:
            raise RuntimeError
        node = self.head
        for _ in range(index):
            node = node.next
        return node.data

    def set_entry(self, index, entry):
        """ Sets the entry at index, raises a RuntimeError otherwise. Even if successful, the length remains the same. """
        if index < 0 or index >= self.length:
            raise RuntimeError
        node = self.head
        for _ in range(index):
            node = node.next
        node.data = entry

    def clear(self):
        """ Empties the list """
        self.head = None
        self.length = 0


L = LinkedList()
L.insert(0, 1)
print(L.head.data)
L.set_entry(0, 2)
print(L.head.data)
