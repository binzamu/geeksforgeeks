# https://practice.geeksforgeeks.org/problems/number-of-ways-to-find-two-numbers/0
t = int(input())

for _ in range(t):
    k = int(input())
    if k % 2 == 0:
        print(int((k / 2 - 1) * (k / 2)))
    else:
        print(int((k - 1) / 2 * (k - 1) / 2))
    