# https://practice.geeksforgeeks.org/problems/minimum-platforms/0
# imos-hou
# If departure time and arrival time is same, I have to count and add the arrival train
# So this code is so complicated.


t = int(input())

for _ in range(t):
    a_time = [0] * 2400
    d_time = [0] * 2400
    n = int(input())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))

    for value in a:
        a_time[value] += 1
    for value in d:
        d_time[value] += 1

    train_num = 0
    max_train_num = 0
    for i in range(len(a_time)):
        if a_time[i] != 0:
            train_num += a_time[i]
            max_train_num = max(train_num, max_train_num)
        if d_time[i] != 0:
            train_num -= d_time[i]
    print(max_train_num)
