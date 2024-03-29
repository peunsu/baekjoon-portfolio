import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

parents = [i for i in range(n+1)]

def find(x: int) -> int:
    if parents[x] == x:
        return x
    return find(parents[x])

def union(x: int, y: int) -> None:
    x = find(x)
    y = find(y)
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

heapify(edges)
sum_cost = 0
edge_cnt = 0
while edge_cnt < n-2:
    cost, u, v = heappop(edges)
    if find(u) != find(v):
        union(u, v)
        sum_cost += cost
        edge_cnt += 1
print(sum_cost)