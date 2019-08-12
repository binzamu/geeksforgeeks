# https://practice.geeksforgeeks.org/problems/find-number-of-numbers/1
def num(arr, n, k):
    arr_separated = []
    for i in arr:
        arr_separated += list(str(i))
    return arr_separated.count(str(k))


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(num(arr, n, k))
# Contributed By: Harshit Sidhwa    