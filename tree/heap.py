class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    # helper methods
    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index -1 ) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    # insert new value
    def insert(self, value):
        """
        MaxHeap insert
        Insert : O(log(n))
        """
        # add element to heap array
        self.heap.append(value)
        current = len(self.heap) -1

        # arrange heap
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    # remove top of heap
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap(max_index, index)
                index = max_index
            else:
                return


myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)
myheap.insert(100)
print(myheap.heap)
myheap.insert(75)
print(myheap.heap)

"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""

myheap1 = MaxHeap()
myheap1.insert(95)
myheap1.insert(75)
myheap1.insert(80)
myheap1.insert(55)
myheap1.insert(60)
myheap1.insert(50)
myheap1.insert(65)

print(myheap1.heap)
myheap1.remove()
print(myheap1.heap)
myheap1.remove()
print(myheap1.heap)
"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]
"""
