import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = set(map(int, input().split()[1:]))
party = [set(map(int, input().split()[1:])) for _ in range(m)]

for _ in range(m):
    for p in party:
        if p.intersection(truth):
            truth = p.union(truth)

cnt = 0
for p in party:
    if not p.intersection(truth):
        cnt += 1
print(cnt)