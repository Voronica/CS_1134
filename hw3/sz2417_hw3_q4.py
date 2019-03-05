def remove_all(lst, value):
    last_value_pos = 0
    for i in range(len(lst)):
        if lst[i] != value:
            lst[i], lst[last_value_pos] = lst[last_value_pos], lst[i]
            last_value_pos += 1
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            lst.pop()
    return lst
