#!/usr/bin/env python3

l = [[1, 'A'], [1, 'B'], [2, 'C']]
d = {}
for key, val in l:
    d.setdefault(key, []).append(val)

print(d)