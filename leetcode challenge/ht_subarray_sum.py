

def subarray_sum(lst, target):
    running_sum = 0
    d = {0:-1}
    for ix, num in enumerate(lst):
        running_sum += num
        complement = running_sum - target
        if complement in d:
            return [d[complement] + 1, ix]
        d[running_sum] = ix
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
