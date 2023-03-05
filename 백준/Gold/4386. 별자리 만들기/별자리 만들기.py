import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

n = int(input())
parents = [i for i in range(n)]

def dist(vec_a, vec_b):
    return sum((b-a)**2 for a, b in zip(vec_a, vec_b)) ** 0.5

def find(x):
    if parents[x] == x:
        return x
    return find(parents[x])

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

coord = [tuple(map(float, input().split())) for _ in range(n)]
edges = []

for i in range(n):
    for j in range(i, n):
        heappush(edges, ([dist(coord[i], coord[j]), i, j]))


sum_dist = 0
while edges:
    d, u, v = heappop(edges)
    if find(u) != find(v):
        union(u, v)
        sum_dist += d

print(round(sum_dist, 2))