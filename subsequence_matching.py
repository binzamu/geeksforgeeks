t = int(input())
for i in range(t):
    s = input()
    while True:
        if s == '':
            print('YES')
            break
        elif s[:3] == 'RYY':
            s = s[3:]
        elif s[:2] == 'RY':
            s = s[2:]
        elif s[:1] == 'R':
            s = s[1:]
        else:
            print('NO')
            break
        # print(s)
