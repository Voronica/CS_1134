def appearances(s, low, high):
    if low > high:
        return {}
    dic = appearances(s,low+1, high)
    if s[low] not in dic:
        dic[s[low]] = 1
        return dic
    else:
        dic[s[low]] += 1
        return dic


