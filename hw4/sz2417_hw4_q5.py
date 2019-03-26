def count_lowercase(s, low, high):
    if low > high:
        return 0
    elif s[low].islower():
        return 1 + count_lowercase(s, low+1, high)
    else:
        return count_lowercase(s, low+1, high)

def is_number_of_lowercase_even(s, low, high):
    count = 0
    if low > high:
        count = 0
    elif s[low].islower():
        count = 1 + count_lowercase(s, low+1, high)
    else:
        count = count_lowercase(s, low+1, high)
    return True if count % 2 == 0 else False

