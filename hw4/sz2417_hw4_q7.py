def split_by_sign(lst, low, high):
    for item in lst:
        if item == 0:
            raise ValueError("Please give list of nonzero numbers!")
    if low >= high:
        return lst
    if lst[low] < 0:
        return [lst[0]] + split_by_sign(lst[1:], low, high - 1)
    else:
        return split_by_sign(lst[1:], low, high - 1) + [lst[0]]



