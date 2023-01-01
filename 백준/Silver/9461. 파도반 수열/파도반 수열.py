import sys

input = sys.stdin.readline

t = int(input())
pn = [1, 1, 1, 2, 2] + [0] * 95
i = 5

for _ in range(t):
    n = int(input())
    while n > i:
        pn[i] = pn[i-5] + pn[i-1]
        i += 1
    print(pn[n-1])