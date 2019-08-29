# https://practice.geeksforgeeks.org/problems/lucky-numbers/0

t = int(input())
input_n = []
for _ in range(t):
    input_n.append(int(input()))

lucky_number = list(range(1, max(input_n) + 1))

i = 2
while i < len(lucky_number):
    j = i - 1
    while j < len(lucky_number):        
        lucky_number.pop(j)
        j += i - 1
    i += 1    

for i in range(len(input_n)):
    if input_n[i] in lucky_number:
        print(1)
    else:
        print(0)
# print(lucky_number)