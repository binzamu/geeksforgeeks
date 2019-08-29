# https://practice.geeksforgeeks.org/problems/where-am-i/0

import math

NESW = ("N", "E", "S", "W")
D = ("U", "R", "D", "L")

def ope(condition_now, processes):
    nesw = NESW.index(condition_now[0])
    direction = D.index(processes[0])
    new_direction = (nesw + direction) % 4
    condition_now[0] = NESW[new_direction]
    condition_now[1][new_direction] += int(processes[1])
    

t = int(input())
for _ in range(t):
    m = int(input())
    input_list = list(input().split())

    processes = []
    condition_now = ["N", [0, 0, 0, 0]]
    for i in range(0, len(input_list) - 1, 2):
        # processes.append([input_list[i], input_list[i + 1]])

        ope(condition_now, [input_list[i], int(input_list[i + 1])])

    position = condition_now[1]
    displacement = int(math.sqrt((position[0] - position[2]) ** 2 + (position[1] - position[3]) ** 2))

    print(displacement, condition_now[0])