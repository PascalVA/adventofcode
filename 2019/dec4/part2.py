#!/usr/bin/env python3

passrange = "134564-585159"

tests = [
    112233,
    123444,
    111122,
    224511,
    111111,
    112233,
    123433,
    556669,
    559999
]


def test_pass(n):
    decreasing = False

    adj_count = 0
    adj_counts = []
    rep_count = 0
    prev = ""

    chars = [int(c) for c in str(n)]
    for i, char in enumerate(chars):
        if prev != "":
            if prev != char:
                adj_counts.append(adj_count)
                rep_count = 0
                adj_count = 0
            rep_count += 1

            if rep_count == 2:
                adj_count += 1
            if rep_count > 2 and adj_count != 0:
                adj_count -= 1

            if prev > char:
                decreasing = True
                break
        else:
            rep_count += 1
        if i == 5:
            adj_counts.append(adj_count)
        prev = char

    return max(adj_counts or [0]) > 0 and not decreasing

for test in tests:
    print(test, test_pass(test))

count = 0
for p in range(134564, 585159 + 1):
    if test_pass(p):
        count += 1
print(count)
