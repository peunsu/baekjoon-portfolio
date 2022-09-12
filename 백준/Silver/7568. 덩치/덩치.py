import sys

input = sys.stdin.readline

n = int(input())
size = [tuple(map(int, input().split())) for _ in range(n)]
rank = [1] * n

for i, s in enumerate(size):
    for ss in size:
        if ss[0] > s[0] and ss[1] > s[1]:
            rank[i] += 1

for r in rank:
    print(r, end=" ")