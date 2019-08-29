# length list store the number that has smaller values in smaller index.

# https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0
t = int(input())

for i in range(t):
    n = int(input())
    given_list = list(map(int, input().split()))
    length_list = [1] * len(given_list)
    for j in range(1, n):
        for k in range(j):
            if given_list[j] > given_list[k] and length_list[j] <= length_list[k]:
                length_list[j] = length_list[k] + 1
    print(max(length_list))


