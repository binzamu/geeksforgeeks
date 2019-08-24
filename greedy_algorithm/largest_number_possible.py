# https://practice.geeksforgeeks.org/problems/largest-number-possible/0

t = int(input())

for i in range(t):
    n, s = map(int, input().split())
    num_9 = s // 9
    if num_9 == 0:
        prefix = ''
    else:
        prefix = "9" * num_9

    if n < num_9 + 1 or s == 0:
        print(-1)
    else:
        print(prefix + str(s - num_9 * 9) + "0" * (n - num_9 - 1))
    

