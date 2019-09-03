# https://practice.geeksforgeeks.org/problems/find-transition-point/1


def search01(arr, start, end):
    if end == start + 1:
        return(start + 1)
    middle = (start + end) // 2
    if arr[middle] == 0:
        return(search01(arr, middle, end))
    elif arr[middle] == 1:
        return(search01(arr, start, middle))


def transitionPoint(arr, n):
    ans = search01(arr, 0, n - 1)
    return(ans)


if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))
# Contirbuted By: Harshit Sidhwa