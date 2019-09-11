def great_common_divider(a, b):
    large = max(a, b)
    small = min(a, b)
    while small != 0:
        large, small = small, large % small

    return large

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    gcd = great_common_divider(a, b)
    
    print(b // gcd, a // gcd)
