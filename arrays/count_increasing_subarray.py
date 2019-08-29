t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # sentinel
    a.append(-1)

    start_index = 0
    subarrays = []
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            if start_index == i:
                pass
            else:
                subarrays.append(a[start_index:i + 1])
            start_index = i + 1
        # print(start_index)
        # print(subarrays)

    ans = 0
    for i in range(len(subarrays)):
        num_component = len(subarrays[i])
        ans += (num_component - 1) * num_component / 2

    print(int(ans))


