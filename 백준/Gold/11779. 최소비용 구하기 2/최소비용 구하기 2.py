import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(s: int, e: int):
    cost = [float('inf')] * (n+1)
    cost[s] = 0
    prev = [None] * (n+1)
    heap = []
    heappush(heap, (0, s))
    while heap:
        c, v = heappop(heap)
        if c > cost[v]:
            continue
        for c_, v_ in graph[v]:
            sum_c = cost[v] + c_
            if cost[v_] > sum_c:
                cost[v_] = sum_c
                prev[v_] = v
                heappush(heap, (cost[v_], v_))
    
    route = [e]
    cur = e
    while cur := prev[cur]:
        route.append(cur)

    return cost[e], route[::-1]

n, m = int(input()), int(input())

graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

cost, route = dijkstra(start, end)

print(cost)
print(len(route))
for r in route:
    print(r, end=" ")