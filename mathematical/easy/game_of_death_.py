t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    # start index is 0
    member = list(range(n + 1))

    start_i = k
    while True:
        if len(member) <= 2:
            break

        if start_i > len(member):
            start_i = start_i - len(member)
            continue

        if start_i <= len(member) - 1:
            member.pop(start_i)
            start_i = start_i + k - 1
        else:
            start_i = k - (len(member) - start_i)
    
    print(*(set(member) - {0}))