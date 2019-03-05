def find_duplicates(lst):
    new_lst_len = max(lst)
    new_lst = [0] * (new_lst_len + 1)
    final_lst = []
    for num in lst:
        new_lst[num] += 1
    for i in range(len(new_lst)):
        if new_lst[i] >= 2:
            final_lst.append(new_lst.index(new_lst[i]))
            new_lst[i] -= 1
    return final_lst

