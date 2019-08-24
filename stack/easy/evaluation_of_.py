# https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression/0
t = int(input())
ope = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}
symbol = ["+", "-", "*", "/"]

for i in range(t):
    s = list(input())
    stack = []
    for j in range(len(s)):
        if s[j] in symbol:
            stack.append(int(ope[s[j]](stack[-2], stack[-1])))
            stack.pop(-3)
            stack.pop(-2)
        else:
            stack.append(int(s[j]))
    
    print(*stack)
