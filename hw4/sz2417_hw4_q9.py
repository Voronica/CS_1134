def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    else:
        lst1 = permutations(lst, low+1, high)
        lst2 = []
        for i in range (len(lst1)):
            for j in range (len(lst1[i])+1):
                ls = lst1[i][:]
                ls.insert(j,lst[low])
                lst2.append(ls)
        return lst2