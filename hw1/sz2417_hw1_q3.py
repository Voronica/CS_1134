def square_sum1(n):
    sum = 0
    for i in range(n):
        sum += i ** 2
    return sum

def square_sum2(n):
    return sum([i ** 2 for i in range(n)])


def square_odd_sum1(n):
    sum = 0
    for i in range(n):
        if i %2 != 0:
            sum += i ** 2
    return sum

def square_odd_sum2(n):
    return sum([i ** 2 for i in range(n) if i % 2 != 0])


def main(): #tester code
    print(square_sum1(5))
    print(square_sum2(5))
    print(square_odd_sum1(5))
    print(square_odd_sum2(5))


