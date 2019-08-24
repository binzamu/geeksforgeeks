# https://practice.geeksforgeeks.org/problems/smallest-number-with-sum-of-digits-as-n-and-divisible-by-10n/0

t = int(input())

for i in range(t):
    n = int(input())
    num_9 = n // 9
    if n % 9 != 0:
        head = str(n - 9 * num_9)
    else:
        head = ""
    print(head + "9" * num_9 + "0" * n)

