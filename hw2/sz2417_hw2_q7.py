def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    ind= None
    found = False
    while (found == False) and (left < right):
        mid = (right + left) // 2
        if (lst01[mid] == 1) and (mid == 0 or lst01[mid - 1] == 0):
            ind = mid
            found = True
        elif lst01[mid] == 1:
            right = mid - 1
        else:
            left = mid + 1
    return ind
