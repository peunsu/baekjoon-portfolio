import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [0] * 101
visited = [0] * 101

for _ in range(n+m):
    a, b = map(int, input().split())
    graph[a] = b

queue = deque([1])
while queue:
    v = queue.popleft()

    if v == 100:
        break

    for i in range(1, 7):
        u = v + i
        if u <= 100:
            if graph[u]:
                u = graph[u]
            if not visited[u]:
                queue.append(u)
                visited[u] = visited[v] + 1

print(visited[100])