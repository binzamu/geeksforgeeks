# https://practice.geeksforgeeks.org/problems/merge-sort/1
# not completed
import math


def devide(arr):
    half_num = math.ceil(len(arr) / 2)
    return list[:half_num], list[half_num]


def merge(arr1, arr2):
    list_merged = []
    while True:
        if not arr1:
            list_merged.extend(arr2)
            return list_merged
        elif not arr2:
            list_merged.extend(arr1)
            return list_merged

        if arr1[0] <= arr2[0]:
            list_merged.apend(arr1[0])
            arr1.pop(0)
        else:
            list_merged.append(arr2[0])
            arr2.pop(0)


def mergeSort(arr):
    arr_1, arr_2 = devide(arr)
    
    while True:


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        mergeSort(arr)
        for i in range(n):
            print(arr[i], end=" ")
        print()