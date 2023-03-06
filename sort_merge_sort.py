"""
Space complexity: O(n)
Time complexity: O(n log(n))
"""


def merge(sorted_list1, sorted_list2):
    combined = []
    i = 0
    j = 0

    while i < len(sorted_list1) and j < len(sorted_list2):
        if sorted_list1[i] < sorted_list2[j]:
            combined.append(sorted_list1[i])
            i += 1
        else:
            combined.append(sorted_list2[j])
            j += 1
    while i < len(sorted_list1):
        combined.append(sorted_list1[i])
        i += 1
    while j < len(sorted_list2):
        combined.append(sorted_list2[j])
        j += 1
    return combined


def merge_sort(list):
    if len(list) == 1:
        return list

    mid = int(len(list) / 2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)


original_list = [4, 2, 6, 5, 1, 3]
sorted_list = merge_sort(original_list)
print("Original List:", original_list)
print("\nSorted List:", sorted_list)
# print(merge([5, 6], [1, 2, 3, 4, 7, 8]))
