"""Given an unsorted array of integers, write a function that finds the length of the
longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater
than the previous element).

Use sets to optimize the runtime of your solution.
Input: An unsorted array of integers, nums.
Output: An integer representing the length of the longest consecutive sequence in nums.
Example:
    Input: nums = [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.
"""


"""Steps:

create hashset from input array
create longest sequence counter
loop all items in given array
    check if its a start of sequence
        loop to check and update local length if next number exists
        update longest sequence counter with max
return longest sequence counter
"""

import pytest
def longest_consecutive_sequence(nums) -> int:
    """
    Using hashset with complexity: O(n)

    """
    set_nums = set(nums)
    longest_seq_length = 0
    for n in nums:
        if n-1 not in set_nums:
            length = 0
            while n+length in set_nums:
                length += 1
            longest_seq_length = max(longest_seq_length, length)
    return longest_seq_length


test_cases = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([1, 3, 15, 17, 18, 23, 25, 30, 41, 42, 43, 44], 4),
    ([9, 1, 2, 9, 0, 10, 5], 3)
]

@pytest.mark.parametrize("nums,expected", test_cases)
def test_longest_consecutive_sequence(nums, expected):
    result = longest_consecutive_sequence(nums)
    assert result == expected