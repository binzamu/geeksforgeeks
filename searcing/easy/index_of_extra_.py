# https://practice.geeksforgeeks.org/problems/index-of-an-extra-element/1

def findExtra(a, b, n):
    x = list(set(a) - set(b))
    if len(x) >= 2:
        return "ERROR"
    else:
        return a.index(x[0])

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(findExtra(a,b,n))