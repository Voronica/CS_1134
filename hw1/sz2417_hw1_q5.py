def fibs(n):
    num1 = 0
    num2 = 1
    for i in range(n):
        yield num2
        num2 = num1 + num2
        num1 = num2 - num1

for curr in fibs(8):
    print(curr , " ", end = "")