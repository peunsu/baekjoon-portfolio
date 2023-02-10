import sys
from heapq import heappush, heappop
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

dist = [float('inf')] * (v+1)
dist[k] = 0

heap = []
heappush(heap, (0, k))
while heap:
    cur_dist, cur_ = heappop(heap)

    if cur_dist > dist[cur_]:
        continue

    for next_dist, next_ in graph[cur_]:
        sum_dist = cur_dist + next_dist
        if sum_dist < dist[next_]:
            dist[next_] = sum_dist
            heappush(heap, (dist[next_], next_))

for d in dist[1:]:
    if d >= float('inf'):
        print("INF")
    else:
        print(d)