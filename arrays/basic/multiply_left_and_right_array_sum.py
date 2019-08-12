# https://practice.geeksforgeeks.org/problems/multiply-left-and-right-array-sum/0
def ope(arr, n):
    devide_index = int(n / 2)
    
    return(sum(arr[:devide_index]) * sum(arr[devide_index:]))

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        # k = int(input())
        print(ope(arr, n))
