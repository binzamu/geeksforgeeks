# https://practice.geeksforgeeks.org/problems/who-will-win/0

# binary tree
test_num = int(input())


def binary_search(list, key, check):
    if len(list) == 0:
        check = True
        # print(-1)
        return check, 0

    div_num = int(len(list) / 2)
    if list[div_num] == key:
        return check, div_num
    elif list[div_num] < key:
        check, index = binary_search(list[div_num + 1:], key, check)
        return check, int(len(list) / 2) + index
    elif list[div_num] > key:
        check, index = binary_search(list[:div_num], key, check)
        return check, index


for i in range(test_num):
    list_num, key = [int(j) for j in input().split()]
    input_list = [int(j) for j in input().split()]
    length_input_list = len(input_list)

    check = False
    check, index = binary_search(input_list, key, check)
    if check is True:
        print(-1)
    else:
        print(1)
