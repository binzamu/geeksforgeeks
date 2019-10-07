t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        n = sum(map(lambda x: int(x) * int(x), str(n)))

        if n == 1:
            print(1)
            break
        elif n == 4:
            print(0)
            break


