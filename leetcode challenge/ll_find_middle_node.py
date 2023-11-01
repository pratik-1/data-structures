class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node_method1(self):
        temp = self.head
        count =0
        l = []
        while temp:
            l.append(temp)
            count += 1
            temp = temp.next
        mid_index = int(count/2)
        return l[mid_index]

    def find_middle_node_method2(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.append(9)

print( my_linked_list.find_middle_node_method1().value )
print( my_linked_list.find_middle_node_method2().value )



"""
    EXPECTED OUTPUT:
    ----------------
    5
    5

"""