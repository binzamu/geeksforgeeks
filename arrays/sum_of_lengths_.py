# https://practice.geeksforgeeks.org/problems/sum-of-lengths-of-non-overlapping-subarrays/0

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    a.insert(0, float("inf"))
    a.append(float("inf"))
    k_indices = [i for i, x in enumerate(a) if x == k]

    # print(k_indices)

    length = 0
    for k_index in k_indices:
        length += 1
        i = 1
        while True:
            if a[k_index - i] <= k:
                length += 1
                i += 1
            else:
                break
        
        i = 1
        while True:
            if a[k_index + i] <= k:
                length += 1
                i += 1
            else:
                break

    print(length)
