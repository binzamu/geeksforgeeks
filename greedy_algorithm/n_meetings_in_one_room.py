# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0
t = int(input())
for i in range(t):
    n = int(input())
    start_times = list(map(int, input().split()))
    finish_times = list(map(int, input().split()))
    f_max = max(finish_times)
    meetings = []
    last_time = 0
    sorted_finish_time = sorted(finish_times)
    for j in sorted_finish_time:
        finish_j = [i for i, n in enumerate(finish_times) if n == j]
        for k in finish_j:
            # print(j, k)
            if start_times[k] >= last_time:
                meetings.append(k + 1)
                last_time = j
                break
    print(*meetings)