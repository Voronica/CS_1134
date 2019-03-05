def split_parity(lst):
    target =0
    for i in range(len(lst)-1):
        if lst[i] % 2 == 1:
            lst[target], lst[i] = lst[i], lst[target]
            target += 1
    return lst
