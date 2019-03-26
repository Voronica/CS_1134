def list_min(lst, low, high):
    if low == high:
        return lst[low]
    else:
        min = list_min(lst, low+1, high)
        if lst[low] < min:
            min = lst[low]
        return min

