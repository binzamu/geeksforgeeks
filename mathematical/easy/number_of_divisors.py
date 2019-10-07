import math
def lcm(a, b):
    return a * b // math.gcd(a, b)

def num_div(n, a, b):
    return n // a + n // b - n // lcm(a, b)

t = int(input())
for _ in range(t):
    n, m, a, b = map(int, input().split())
    print(num_div(m, a, b) - num_div(n - 1, a, b))