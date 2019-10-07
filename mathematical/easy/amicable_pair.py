def create_divisor_set(a):
    divisor_set = {1}
    n = 2
    while n * n <= a:
        if a % n == 0:
            divisor_set.add(n)
            divisor_set.add(a // n)
        n += 1
    return divisor_set


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    divisor_set_a = create_divisor_set(a)
    divisor_set_b = create_divisor_set(b)

    if sum(divisor_set_a) == b and sum(divisor_set_b) == a:
        print(1)
    else:
        print(0)

