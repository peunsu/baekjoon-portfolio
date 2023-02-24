import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

parents = [i for i in range(v+1)]

def find(x: int):
    if parents[x] == x:
        return x
    return find(parents[x])

def union(x: int, y: int):
    x_parent = find(x)
    y_parent = find(y)
    if x_parent < y_parent:
        parents[y_parent] = x_parent
    else:
        parents[x_parent] = y_parent

heapify(edges)
sum_cost = 0
while edges:
    cost, u, v = heappop(edges)
    if find(u) != find(v):
        union(u, v)
        sum_cost += cost

print(sum_cost)