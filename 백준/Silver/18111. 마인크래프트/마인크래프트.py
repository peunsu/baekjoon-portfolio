import sys
from itertools import chain
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().split())
coord = [list(map(int, input().split())) for _ in range(n)]
coord = Counter(list(chain(*coord)))

times = []

for i in range(min(coord.keys()), max(coord.keys()) + 1):
    diff = [(i - c) * n for c, n in coord.items()]
    if sum(diff) > b:
        continue
    times.append([sum([d if d >= 0 else -d * 2 for d in diff]), i])
times.sort(key=lambda x: -x[1])
times.sort(key=lambda x: x[0])

print(*times[0], sep=" ")