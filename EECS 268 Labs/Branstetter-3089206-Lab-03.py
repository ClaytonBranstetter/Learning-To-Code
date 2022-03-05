'''
Author: Clayton Branstetter
KUID: 3089206
Date: 02/28/2022
Lab: lab#03
Last modified: 03/04/2022
Purpose: Mock CPU Scheduler
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, entry):
        """ Put the entry at the top of the Stack."""
        node = Node(entry)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def is_empty(self):
        """ Return True if Stack is empty, False otherwise."""
        return self.length == 0

    def peek(self):
        """ Return value at the top of the Stack, raise a RuntimeError otherwise."""
        if self.is_empty():
            raise RuntimeError
        return self.head.value

    def pop(self):
        """ Remove and return the value at the top of the stack. Raise RuntimeError otherwise."""
        if self.is_empty():
            raise RuntimeError
        self.head = self.head.next
        self.length -= 1


class Queue:
    def __init__(self):
        self.head = None
        self.length = 0

    def enqueue(self, entry):
        """ Put the entry at the back of the Queue."""
        new_node = Node(entry)
        if self.is_empty():
            self.head = new_node
        else:
            head = self.head
            while head.next != None:
                head = head.next
            head.next = new_node
        self.length += 1

    def is_empty(self):
        """ Return True if Queue is empty, False otherwise."""
        return self.length == 0

    def peek_front(self):
        """ Return value at the front of the queue, raise a RuntimeError otherwise."""
        if self.is_empty():
            raise RuntimeError
        head = self.head
        return head.value

    def dequeue(self):
        """ Remove and return the value at the front of the Queue. Raise RuntimeError otherwise."""
        if self.is_empty():
            raise RuntimeError
        self.head = self.head.next
        self.length -= 1


def clean_file(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        rows = data.split('\n')
        while '' in rows:
            rows.remove('')
    commands, processes = [], []
    for row in rows:
        row_list = row.strip().split()
        commands.append(row_list[0])
        if row_list[0] != 'RETURN':
            processes.append(row_list[1])
    return commands, processes


class cpu:
    def __init__(self, commands, processes):
        self.stack = Stack()
        self.queue = Queue()
        self.commands = commands
        self.processes = processes

    def START(self, process):
        """ A new process is created and added to the queue. All processes start with a "main" as their first function call. Print a message to the screen indicating which process was added to the queue."""
        self.queue.enqueue(process)
        print(f'{process} added to queue')

    def CALL(self, function):
        """ The process at the front of the queue gets some CPU time and calls a function. This put that function on the call stack for that process. After the call is made, that process goes to the back of the line. Print a message to the screen indicating which process called the function and what the name of the function is."""
        self.stack.push(function)
        process = self.queue.peek_front()
        self.queue.dequeue()
        self.stack.pop()
        print(f'{process} calls {function}')

    def RETURN(self):
        """ The process at the front of the queue has the function at the top of its call-stack return. If the process has any functions left on the call-stack, put it at the back of the queue. Otherwise, if its main returns, simply remove it. Should a process end, display a message indicating this."""
        process = self.queue.peek_front()
        self.queue.dequeue()
        print(f'{process} returns from main')
        print(f'{process} process has ended')

    def run(self):
        commands = self.commands
        processes = self.processes + ['']
        for command, process in zip(commands, processes):
            if command == 'START':
                self.START(process)
            elif command == 'CALL':
                self.CALL(process)
            elif command == 'RETURN':
                self.RETURN()
            else:
                print('Unvalid command')


def main():
    file_name = input(" Enter the name of the input file: ")
    commands, processes = clean_file(file_name)
    cpu(commands, processes).run()


main()
