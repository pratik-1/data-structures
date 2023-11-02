"""
Swap the values of the first and last node

Note that the pointers to the nodes themselves are not swapped - only their values are exchanged
"""

from hmac import new


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) -> None:
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next

    def append(self, value) -> None:
        new_node = Node(value)
        if self.length == 0:
             self.head = new_node
             self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # WRITE SWAP_FIRST_LAST METHOD HERE #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################
    def swap_first_last(self):
        self.head.value, self.tail.value = self.tail.value, self.head.value


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)


print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.swap_first_last()


print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1

"""

