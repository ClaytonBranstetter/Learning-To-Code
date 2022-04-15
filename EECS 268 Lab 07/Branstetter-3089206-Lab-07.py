'''
Author: Clayton Branstetter
KUID: 3089206
Date: 04/05/2022
Lab: lab#07
Last modified: 04/15/2022
Purpose: Timing Functions
'''

import time
from DataStructure import *

def nanosec_to_sec(ns):
    BILLION = 1000000000
    return ns/BILLION

def pop_one(n):
    """Popping a single item from a stack"""
    list_time = [] #recording time
    #increasing the size by 1000 each time
    for i in range(1,n//1000 + 1):
        stack = Stack()
        start_time = time.process_time_ns()
        #push 1000*i
        for j in range(1,i*1000+1):
            stack.push(j)
        stack.pop()
        end_time = time.process_time_ns()
        list_time.append(nanosec_to_sec(end_time-start_time))
    return list_time

def pop_all(n):
    """Popping all items from a stack"""
    list_time = []
    for i in range(1,n//1000 + 1):
        stack = Stack()
        start_time = time.process_time_ns()
        for j in range(1,i*1000+1):
            stack.push(j)
        for _ in range(1,i*1000+1):
            stack.pop()
        end_time = time.process_time_ns()
        list_time.append(nanosec_to_sec(end_time-start_time))
    return list_time

def Q_enqueue(n):
    """Queue's enqueue"""
    list_time = []
    for i in range(1,n//1000 + 1):
        queue = Queue()
        start_time = time.process_time_ns()
        for j in range(1,i*1000+1):
            queue.enqueue(j)
        end_time = time.process_time_ns()
        list_time.append(nanosec_to_sec(end_time-start_time))
    return list_time

def L_entry_0(n):
    """Linked List get_entry at specifically index 0"""
    list_time = []
    for i in range(1,n//1000 + 1):
        List = LinkedList()
        start_time = time.process_time_ns()
        for j in range(1,i*1000+1):
            List.insert(0, j)
        List.get_entry(0)
        end_time = time.process_time_ns()
        list_time.append(nanosec_to_sec(end_time-start_time))
    return list_time

def L_entry_last(n):
    """Linked List get_entry at specifically the last index"""
    list_time = []
    for i in range(1,n//1000 + 1):
        List = LinkedList()
        start_time = time.process_time_ns()
        for j in range(1,i*1000+1):
            List.insert(0, j)
        List.get_entry(List.length-1)
        end_time = time.process_time_ns()
        list_time.append(nanosec_to_sec(end_time-start_time))
    return list_time

def L_entry_all(n):
    """Printing all elements in a LinkedList using get_entry"""
    list_time = []
    for i in range(1,n//1000 + 1):
        List = LinkedList()
        start_time = time.process_time_ns()

        for j in range(1,i*1000+1):
            List.insert(j-1, j)

        for j in range(i*1000): #print all items
            print(List.get_entry(j))
        end_time = time.process_time_ns()
        list_time.append(nanosec_to_sec(end_time-start_time))
    return list_time

def main():
    n = 100000
    print('\n\nPopping a single item from a stack\n\n')
    print(pop_one(n))
    print('\n\nPopping all items from a stack\n\n')
    print(pop_all(n))
    print("\n\nQueue's enqueue\n\n")
    print(Q_enqueue(n))
    print('\n\nLinked List get_entry at specifically index 0\n\n')
    print(L_entry_0(n))
    print('\n\nLinked List get_entry at specifically the last index\n\n')
    print(L_entry_last(n))
    print('\n\nPrinting all elements in a LinkedList using get_entry\n\n')
    print(L_entry_all(n))

main()
