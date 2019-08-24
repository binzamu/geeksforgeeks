# https://practice.geeksforgeeks.org/problems/activity-selection/0

t = int(input())

for i in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    activities = {}
    for i in range(len(start)):
        if end[i] in activities.keys():
            activities[end[i]] = max(start[i], activities[end[i]])
        else:
            activities[end[i]] = start[i]
    
    ans = 0
    end_time = 0
    for i in sorted(activities):
        # print(i, activities[i])
        if activities[i] >= end_time:
            end_time = i
            ans += 1

    print(ans)