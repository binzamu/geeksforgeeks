# https://practice.geeksforgeeks.org/problems/min-sum-formed-by-digits/0
t = int(input())
for i in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    a = []
    b = []
    for j in range(int((n + 1) / 2)):
        a.append(str(arr[2 * j]))
        if 2 * j + 1 == n:
            break
        b.append(str(arr[2 * j + 1]))
    a_num = int("".join(a))
    b_num = int("".join(b))
    print(a_num + b_num)