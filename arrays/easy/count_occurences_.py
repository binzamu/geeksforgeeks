# https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams/0


# import itertools
import collections

t = int(input())

for i in range(t):
    c = input()
    s = input()

    stored = dict(collections.Counter(s))
    # s_per = itertools.permutations(s)
    # s_char_list = set(s)
    # s_per_list = [''.join(list(i)) for i in set(s_per)]

    s_len = len(s)
    # count = collections.Counter(c)
    count = 0
    j = 0
    while j <= len(c) - s_len:
        if dict(collections.Counter(c[j:j + s_len])) == stored:
            count += 1
        j += 1
        # if c[j + s_len - 1] not in s_char_list:
        #     j += s_len
        #     # print(s_char_list)
        #     # print(c[j])
        #     continue
        # if c[j:j + s_len] in s_per_list:
        #     # print(c[j:j + s_len])
        #     count += 1
        #     j += 1
        # else:
        #     j += 1
    print(count)
