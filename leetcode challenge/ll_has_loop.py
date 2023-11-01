"""
Write a method called has_loop that is part of the linked list class.
The method should be able to detect if there is a cycle or loop present in the linked list.

The method should utilize `Floyd's cycle-finding algorithm`, also known as the "tortoise and hare" algorithm,
to determine the presence of a loop efficiently.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # WRITE HAS_LOOP METHOD HERE #
    def has_loop(self):
        slow = self.head
        fast = self.head

        while (slow is not None and fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False





my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
# my_linked_list_2.print_list()
print(my_linked_list_2.has_loop() ) # Returns False


my_linked_list_3 = LinkedList(1)
my_linked_list_3.append(2)
my_linked_list_3.append(3)
my_linked_list_3.append(4)
my_linked_list_3.tail.next = my_linked_list_3.get(2)
# my_linked_list_3.print_list()
print(my_linked_list_3.has_loop() ) # Returns True

"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
"""
