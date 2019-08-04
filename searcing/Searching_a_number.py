# https://practice.geeksforgeeks.org/problems/searching-a-number/0

test_num = int(input())

for i in range(test_num):
    list_num, key = [int(j) for j in input().split()]
    input_list = [int(j) for j in input().split()]
    for k, item in enumerate(input_list):
        if item == key:
            print(k + 1)
            break

        if k == len(input_list) - 1:
            print(-1)
            break
