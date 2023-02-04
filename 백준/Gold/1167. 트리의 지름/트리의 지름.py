import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(v: int, dist: int):
    global max_dist, furthest

    visited[v] = 1

    if dist > max_dist:
        max_dist = dist
        furthest = v

    for u, d in graph[v]:
        if not visited[u]:
            dfs(u, dist + d)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n):
    v, *dist = map(int, input().split()[:-1])
    for i in range(0, len(dist), 2):
        graph[v].append((dist[i], dist[i+1]))

max_dist, furthest = 0, 0
dfs(1, 0)

max_dist = 0
visited = [0] * (n+1)
dfs(furthest, 0)

print(max_dist)