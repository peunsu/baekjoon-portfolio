import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
costs = [float('inf')] * (n+1)

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

start, end = map(int, input().split())

heap = []
costs[start] = 0
heappush(heap, (0, start))

while heap:
    c, v = heappop(heap)
    
    if v == end:
        break

    for c_, v_ in graph[v]:
        cost_ = costs[v] + c_
        if cost_ < costs[v_]:
            costs[v_] = cost_
            heappush(heap, (costs[v_], v_))

print(costs[end])