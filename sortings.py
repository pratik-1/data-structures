def bubble_sort(lst):
    """Time complexity: O(n^2)"""
    for j in range(len(lst) - 1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def selection_sort(lst):
    """Time complexity: O(n^2)"""
    for j in range(len(lst) - 1):
        min_index = j
        for i in range(j + 1, len(lst)):
            if lst[min_index] > lst[i]:
                min_index = i
        if j != min_index:
            lst[min_index], lst[j] = lst[j], lst[min_index]
    return lst


def insertion_sort(lst):
    """
    Time complexity: O(n^2)
    Best case when list is almost sorted: Omega(n)
    """

    for i in range(1, len(lst)):
        ## While Loop
        temp = i - 1
        while (lst[temp] > lst[i]) and (temp > -1):
            lst[i], lst[temp] = lst[temp], lst[i]
            i = temp
            temp -= 1

        ## For loop
        for j in range(i - 1, -1, -1):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                i = j
    return lst


print("Sort list:", [4, 2, 6, 5, 1, 3])
print("Bubble sort:", bubble_sort([4, 2, 6, 5, 1, 3]))
print("Selection sort:", selection_sort([4, 2, 6, 5, 1, 3]))
print("Insertion sort:", insertion_sort([4, 2, 6, 5, 1, 3]))
