import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

sum_c = 0
visited = [0] * (v+1)
visited[1] = 1
heap = graph[1]
heapify(heap)
while heap:
    c, u = heappop(heap)

    if visited[u]:
        continue

    visited[u] = 1
    sum_c += c
    for c_, u_ in graph[u]:
        if not visited[u_]:
            heappush(heap, (c_, u_))

print(sum_c)