import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start: int, end: int):
    dist = [float('inf')] * (n+1)
    dist[start] = 0

    heap = []
    heappush(heap, (0, start))
    while heap:
        cur_dist, cur_ = heappop(heap)

        if cur_ == end:
            break

        if cur_dist > dist[cur_]:
            continue

        for next_dist, next_ in graph[cur_]:
            sum_dist = cur_dist + next_dist
            if sum_dist < dist[next_]:
                dist[next_] = sum_dist
                heappush(heap, (dist[next_], next_))

    return dist[end]

n, e = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

pt1, pt2 = map(int, input().split())

result = dijkstra(pt1, pt2) + min(dijkstra(1, pt1) + dijkstra(pt2, n), dijkstra(1, pt2) + dijkstra(pt1, n))

if result >= float('inf'):
    print(-1)
else:
    print(result)