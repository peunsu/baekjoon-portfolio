import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    clothes = []

    for _ in range(n):
        clothes.append(input().split()[1])
    
    clothes = Counter(clothes).values()

    tot = 1
    for c in clothes:
        tot *= (c+1)
    print(tot-1)