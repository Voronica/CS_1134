import math

def factors(num):
    for x in range(1,int(math.sqrt(num))+1):
        if num % x == 0:
            yield x
    for x in range(int(math.sqrt(num))-1, 0, -1):
        if num % x == 0:
            yield num // x

