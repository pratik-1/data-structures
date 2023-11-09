def pivot(list):
    """
    Time Complexity: O(n)
    """
    # pivot
    pivot = list[0]
    # pivot replace index
    gt = 0

    # arrange items around pivot value
    for i, v in enumerate(list[1:]):
        if v < pivot:
            j = list.pop(i + 1)
            list.insert(0, j)
            gt += 1

    # swap
    pivot, list[gt] = list[gt], pivot
    return list, gt


def quick_sort(list):
    """
    Time Complexity:
    n from pivot and log n from function itself
        = Omega and Theta(n log n)
        = O(n^2)
    """
    if len(list) <= 1:
        return list
    list, gt = pivot(list)
    # repeat recursively on left and right of pivot
    list[0:gt] = quick_sort(list[0:gt])
    list[gt + 1 :] = quick_sort(list[gt + 1 :])

    return list


my_list = [6, 5, 2, 4, 1, 3]
my_sorted_list = quick_sort(my_list)
print(my_sorted_list)
