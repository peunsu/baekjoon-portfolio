import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start: int):
    cost = [float('inf')] * (n+1)
    cost[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        c, v = heappop(heap)
        if c > cost[v]:
            continue

        for c_, v_ in graph[v]:
            sum_c = cost[v] + c_
            if cost[v_] > sum_c:
                cost[v_] = sum_c
                heappush(heap, (cost[v_], v_))
    
    return cost[1:]

n, m, x = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))

costs = []
for i in range(1, n+1):
    costs.append(dijkstra(i))

print(max(costs[i][x-1] + costs[x-1][i] for i in range(n)))