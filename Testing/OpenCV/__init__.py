def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]  # moves pivot to the end
    store_index = start
    for i in xrange(start, end):
        if lst[i] < lst[end]:  # if smaller than pivot swap
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]  # puts pivot in its right place
    return store_index  # return pivot index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = start + (end - start) / 2  # chooses middle value to be pivot
    new_pivot = partition(lst, start, end, pivot)  # gets new pivot location
    quick_sort(lst, start, new_pivot - 1)  # sort list below pivot
    quick_sort(lst, new_pivot + 1, end)  # sort list above pivot


def sort(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst


print sort([-5, 3, -2, 7, 10, 3, 19, 5])  # sort this list
