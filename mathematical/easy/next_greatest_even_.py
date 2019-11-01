t = int(input())
for _ in range(t):
    n = input()
    for i in range(len(n) - 2, -1, -1):
        v_larger_i = [v for v in n[i + 1:] if v > n[i]]
        v
        if len(v_larger_i) >= 1 and any([v % 2 == 0 for v in v_larger_i]):
            ans_string = min(v_larger_i)
            backchars = list(n[i:])
            backchars.remove(ans_string)
            backchars = ''.join(sorted(backchars))
            # v_larger_i.append(n[i])
            # v_larger_i.sort()
            ans_string = n[:i] + ans_string + backchars
            break
    
    print(ans_string)
# if n[i] % 2 == 0 and any([v > n[-1] for v in n[i:]]):


