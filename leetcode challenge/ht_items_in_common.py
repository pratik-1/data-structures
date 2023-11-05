"""
Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.

Solve in O(n) time complexity.
"""

def items_in_common(list1, list2) -> bool:
    my_dict = {}
    for i in list1:
        my_dict.setdefault(i,None)
    for i in list2:
        if i in my_dict:
            return True
    return False


a = [1,2,3,4,5]
b = [3,4,5,6,7]

print(items_in_common(a,b))