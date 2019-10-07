def create_divisor_set(a):
    divisor_set = [1]
    n = 2
    while n * n < a:
        if a % n == 0:
            divisor_set.append(n)
            divisor_set.append(a // n)
        n += 1
    
    if n * n == a:
        divisor_set.append(n)
    divisor_set.sort()
    return divisor_set


t = int(input())
for _ in range(t):
    n = int(input())
    divisor_set = create_divisor_set(n)
    divisor_set.append(n)
    ans = 0
    for v in divisor_set:
        sub_divsor_set = create_divisor_set(v)
        if v != 1:
            sub_divsor_set.append(v)
        ans += sum(sub_divsor_set)

    print(ans)
    