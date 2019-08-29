def extract(s, tmp_s, permu_list):
    # print('s', s, 'tmp_s', tmp_s, 'permu_list', permu_list)
    if s == '':
        permu_list.append(tmp_s)
        tmp_s = tmp_s[:-1]
        # print('last', tmp_s)
    else:
        for i, value in enumerate(s):
            tmp_s = tmp_s + value
            s_list = list(s)
            del s_list[i]
            # print(''.join(s_list))
            # print('before', tmp_s)
            extract(''.join(s_list), tmp_s, permu_list)
            tmp_s = tmp_s[:-1]
            # print('after', tmp_s)

    # tmp_s[:-1]


t = int(input())
for i in range(t):
    s = input()
    s = ''.join(sorted(list(s)))
    permu_list = []
    extract(s, '', permu_list)

    print(*permu_list)