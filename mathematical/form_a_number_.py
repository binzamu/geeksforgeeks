# https://practice.geeksforgeeks.org/problems/form-a-number-divisible-by-3-using-array-digits/0

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(list, input().split()))

    sum_digit = 0
    for i in range(len(a)):
        sum_digit += sum(list(map(int, a[i])))
    if sum_digit % 3 == 0:
        print(1)
    else:
        print(0)
    # sum_digit = sum(list(map(lambda x: list(str(x)), a)))


