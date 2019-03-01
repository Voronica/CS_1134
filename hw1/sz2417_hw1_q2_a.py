def shift(lst, k):
    for i in range(k):
        lst.append(lst[0])
        del lst[0]
    return lst

