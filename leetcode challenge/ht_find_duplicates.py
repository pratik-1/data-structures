"""
Problem: Given an array of integers nums, find all the duplicates in the array.


Input:

    A list of integers nums.


Output:

    A list of integers representing the numbers in the input array nums that appear more than once.
    If no duplicates are found in the input array, return an empty list [].


    Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
    Output: [2, 3]
    Explanation: The numbers 2 and 3 appear more than once in the input array.

    Input: nums = [1, 2, 3, 4, 5]
    Output: []
    Explanation: There are no duplicates in the input array, so the function returns an empty list [].

    Input: nums = [3, 3, 3, 3, 3]
    Output: [3]
    Explanation: The number 3 appears more than once in the input array.

    Input: nums = [-1, 0, 1, 0, -1, -1, 2, 2]
    Output: [-1, 0, 2]
    Explanation: The numbers -1, 0, and 2 appear more than once in the input array.

    Input: nums = []
    Output: []
    Explanation: There are no numbers in the input array, so the function returns an empty list [].
"""

def find_duplicates(lst) -> list:
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d.setdefault(i,1)
    # op = []
    # for k,v in d.items():
    #     if v > 1:
    #         op.append(k)
    #         continue
    op = [k for k,v in d.items() if v > 1]
    return op



print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

