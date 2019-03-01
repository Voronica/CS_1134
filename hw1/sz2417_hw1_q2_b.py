def shift(lst, k, dir = "left"):
    if dir == "left":
        for i in range(k):
            lst.append(lst[0])
            del lst[0]
        return lst
    elif dir == "right":
        for i in range(k):
            lst.insert(0,lst[-1])
            del lst[-1]
        return lst
    else:
        print("Direction not valid!")








