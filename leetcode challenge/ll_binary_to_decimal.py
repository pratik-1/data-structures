"""
Your task is to implement the binary_to_decimal method for the LinkedList class.
This method should convert a binary number, represented as a linked list, to its decimal equivalent.

In this context, a binary number is a sequence of 0s and 1s. The LinkedList class represents
 this binary number such that each node in the linked list contains a single digit (0 or 1) of
 the binary number, and the whole number is formed by traversing the linked list from the head to the end.

The binary_to_decimal method should start from the head of the linked list and use each node's value to
 calculate the corresponding decimal number. The formula to convert a binary number to decimal is as follows:

    1) Each digit of the binary number is multiplied by 2 raised to the power
    equivalent to the position of the digit, counting from right to left starting from 0.
    2) All the results are summed together to get the decimal number.
    3) The binary_to_decimal method should return this calculated decimal number.

Examples
Consider the binary number 101. If this number is represented as a linked list,
the head of the linked list will contain the digit 1, the next node will contain 0,
and the last node will contain 1. When we apply the binary_to_decimal method on this linked list,
the method should return the number 5, which is the decimal equivalent of binary 101.

Similarly, for a linked list 1->1->0->1, the binary_to_decimal should return the number 13.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) -> None:
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_all(self):
        if self.length == 0:
            print("Head: None")
        else:
            print("Head: ", self.head.value)
        print("Length: ", self.length)
        print("\nLinked List:")
        if self.length == 0:
            print("empty")
        else:
            self.print_list()

    def reversed_list(self):
        # reverse head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # reverse pointers
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # WRITE BINARY_TO_DECIMAL METHOD HERE #
    def binary_to_decimal(self) -> int:
        decimal = 0
        temp = self.head
        for ix in range(self.length):
            decimal = decimal * 2 + temp.value
            temp = temp.next
        return decimal


# Test case 1: Binary number 110 = Decimal number 6
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 6
    print("Test case 1 passed, returned: ", result)
except AssertionError:
    print("Test case 1 failed, returned: ", result)

# Test case 2: Binary number 1000 = Decimal number 8
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 8
    print("Test case 2 passed, returned: ", result)
except AssertionError:
    print("Test case 2 failed, returned: ", result)

# Test case 3: Binary number 0 = Decimal number 0
linked_list = LinkedList(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 0
    print("Test case 3 passed, returned: ", result)
except AssertionError:
    print("Test case 3 failed, returned: ", result)

# Test case 4: Binary number 1 = Decimal number 1
linked_list = LinkedList(1)
result = linked_list.binary_to_decimal()
try:
    assert result == 1
    print("Test case 4 passed, returned: ", result)
except AssertionError:
    print("Test case 4 failed, returned: ", result)

# Test case 5: Binary number 1101 = Decimal number 13
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
result = linked_list.binary_to_decimal()
try:
    assert result == 13
    print("Test case 5 passed, returned: ", result)
except AssertionError:
    print("Test case 5 failed, returned: ", result)


"""
    EXPECTED OUTPUT:
    ----------------
    Test case 1 passed, returned:  6
    Test case 2 passed, returned:  8
    Test case 3 passed, returned:  0
    Test case 4 passed, returned:  1
    Test case 5 passed, returned:  13
"""
