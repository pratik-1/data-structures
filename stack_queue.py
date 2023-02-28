class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height > 0:
            new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.last = None
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp


my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop().value)

print("\nStack after pop():")
my_stack.print_stack()


"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    1
    2
    3
    4

    Popped node:
    1

    Stack after pop():
    2
    3
    4

"""


my_queue = Queue(1)

print("Queue before enqueue(2):")
my_queue.print_queue()

my_queue.enqueue(2)

print("\nQueue after enqueue(2):")
my_queue.print_queue()


"""
    EXPECTED OUTPUT:
    ----------------
    Queue before enqueue(2):
    1

    Queue after enqueue(2):
    1
    2

"""
my_queue = Queue(1)
my_queue.enqueue(2)


print(my_queue.dequeue().value)
print(my_queue.dequeue().value)
print(my_queue.dequeue())
"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""
