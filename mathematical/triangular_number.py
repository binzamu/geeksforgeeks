# https://practice.geeksforgeeks.org/problems/triangular-number/0

def add_triangular_numbers(triangular_numbers, n):
    while triangular_numbers[-1] < n:
        triangular_numbers.append(triangular_numbers[-1] + (len(triangular_numbers) + 1))
        
t = int(input())
for _ in range(t):
    n = int(input())
    triangular_numbers = [1]

    if n > triangular_numbers[-1]:
        add_triangular_numbers(triangular_numbers, n)
    if n in triangular_numbers:
        print(1)
    else:
        print(0)