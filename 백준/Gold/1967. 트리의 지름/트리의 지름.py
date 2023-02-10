import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start: int) -> tuple:
    dist = [float('inf')] * (n+1)
    dist[start] = 0

    heap = []
    heappush(heap, (0, start))
    while heap:
        cur_dist, cur_ = heappop(heap)

        if cur_dist > dist[cur_]:
            continue

        for next_dist, next_ in graph[cur_]:
            sum_dist = cur_dist + next_dist
            if sum_dist < dist[next_]:
                dist[next_] = sum_dist
                heappush(heap, (sum_dist, next_))
    
    max_dist = max(dist[1:])
    max_idx = dist.index(max_dist)

    return max_dist, max_idx


n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

_, next_ = dijkstra(1)
result, _ = dijkstra(next_)
print(result)