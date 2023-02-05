import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = set(map(int, input().split()[1:]))
party = [set(map(int, input().split()[1:])) for _ in range(m)]
know = [0] * m

for i in range(m):
    for j, p in enumerate(party):
        if p.intersection(truth):
            know[j] = 1
            truth = p.union(truth)

print(know.count(0))