# https://practice.geeksforgeeks.org/problems/mr-modulo-and-pairs/0#ExpectOP

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i] < k:
            continue
        else:
            for j in range(n):
                if a[i] % a[j] == k:
                    ans += 1

    print(ans)