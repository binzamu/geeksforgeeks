# https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array/0

# filter not zero list and count the number of zero and add zero list

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    non_zero_list = list(filter(lambda v: v != 0, a))
    ans_list = non_zero_list + [0] * (len(a) - len(non_zero_list))
    print(*ans_list)