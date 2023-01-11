import sys
from collections import deque

input = sys.stdin.readline

def dfs(v: int) -> None:
    visited_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n + 1):
        if visited_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v: int) -> None:
    visited_bfs[v] = 1
    q = deque([v])
    while q:
        i = q.popleft()
        print(i, end=" ")
        for j in range(1, n + 1):
            if visited_bfs[j] == 0 and graph[i][j] == 1:
                q.append(j)
                visited_bfs[j] = 1


n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = graph[j][i] = 1

visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)

dfs(v)
print()
bfs(v)