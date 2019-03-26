def flat_list(nested_lst, low, high):
    lst = []
    if isinstance(nested_lst, list):
        for i in range(low, high+1):
            if isinstance(nested_lst[i], list):
                lst.extend(flat_list(nested_lst[i], 0, len(nested_lst[i])-1))
            else:
                lst.append(nested_lst[i])
    else:
        return nested_lst

    return lst




